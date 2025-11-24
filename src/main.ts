import { app, BrowserWindow, ipcMain } from "electron";
import path from "path";
import { spawn } from "child_process";

let win: BrowserWindow | null = null;
let py: ReturnType<typeof spawn> | null = null;

function createWindow() {
  win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  win.loadFile(path.join(__dirname, "../frontend/index.html"));

  // Start Python with unbuffered output
  py = spawn("python", ["-u", path.join(__dirname, "../python/engine.py")], {
    stdio: ['pipe', 'pipe', 'pipe']
  });

  // Forward Python output to renderer
  py.stdout?.on("data", (data) => {
    const text = data.toString();
    console.log("NODE GOT:", JSON.stringify(text));
    if (win && !win.isDestroyed()) {
      win.webContents.send("py-out", text);
    }
  });

  py.stderr?.on("data", (data) => {
    const errorText = data.toString();
    console.error("Python stderr:", errorText);
    if (win && !win.isDestroyed()) {
      win.webContents.send("py-out", `[ERROR] ${errorText}`);
    }
  });

  py.on("error", (error) => {
    console.error("Failed to start Python:", error);
    if (win && !win.isDestroyed()) {
      win.webContents.send("py-out", `[ERROR] Failed to start Python: ${error.message}\n`);
    }
  });

  py.on("exit", (code, signal) => {
    console.error(`Python process exited with code ${code}, signal ${signal}`);
    if (win && !win.isDestroyed()) {
      win.webContents.send("py-out", `[ERROR] Python process exited unexpectedly (code: ${code})\n`);
    }
  });
}

app.on('window-all-closed', () => {
  if (py) {
    py.kill();
  }
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

// Receive text from renderer → send to Python
ipcMain.handle("py-in", async (_event, text: string) => {
  if (!py) {
    console.error("Python process is null");
    return { success: false, error: "Python process not started" };
  }
  
  if (!py.stdin) {
    console.error("Python stdin is null");
    return { success: false, error: "Python stdin not available" };
  }
  
  if (py.killed) {
    console.error("Python process was killed");
    return { success: false, error: "Python process was killed" };
  }
  
  try {
    const command = text.trim() + "\n";
    console.log("Sending to Python:", JSON.stringify(command));
    const written = py.stdin.write(command);
    if (!written && py.stdin) {
      console.warn("Write buffer is full, waiting for drain");
      await new Promise((resolve) => {
        if (py && py.stdin) {
          py.stdin.once("drain", resolve);
        } else {
          resolve(undefined);
        }
      });
    }
    return { success: true };
  } catch (error: any) {
    console.error("Error writing to Python stdin:", error);
    return { success: false, error: error.message || "Failed to send command" };
  }
});

app.whenReady().then(createWindow);
