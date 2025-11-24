import { app, BrowserWindow, ipcMain } from 'electron';
import * as path from 'path';
import { spawn } from 'child_process';

let mainWindow: BrowserWindow | null = null;
let pythonProcess: ReturnType<typeof spawn> | null = null;

function createWindow(): void {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  mainWindow.loadFile(path.join(__dirname, '../frontend/index.html'));

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

function startPythonEngine(): void {
  const pythonExecutable = process.platform === 'win32' 
    ? 'python.exe' 
    : 'python';
  const pythonPath = path.join(__dirname, '../python/venv', 
    process.platform === 'win32' ? 'Scripts' : 'bin', pythonExecutable);
  const scriptPath = path.join(__dirname, '../python/engine.py');

  pythonProcess = spawn(pythonPath, [scriptPath], {
    stdio: ['pipe', 'pipe', 'pipe'],
  });

  pythonProcess.stdout?.on('data', (data) => {
    console.log(`Python stdout: ${data}`);
    if (mainWindow) {
      mainWindow.webContents.send('python-output', data.toString());
    }
  });

  pythonProcess.stderr?.on('data', (data) => {
    console.error(`Python stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python process exited with code ${code}`);
  });
}

app.whenReady().then(() => {
  createWindow();
  startPythonEngine();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (pythonProcess) {
    pythonProcess.kill();
  }
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

// Handle IPC communication
ipcMain.handle('send-to-python', async (_event, data: string) => {
  if (pythonProcess && pythonProcess.stdin) {
    pythonProcess.stdin.write(data + '\n');
    return { success: true };
  }
  return { success: false, error: 'Python process not available' };
});

