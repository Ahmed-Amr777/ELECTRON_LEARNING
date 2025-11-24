import { contextBridge, ipcRenderer } from 'electron';

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  sendToPython: (data: string) => ipcRenderer.invoke('send-to-python', data),
  onPythonOutput: (callback: (data: string) => void) => {
    ipcRenderer.on('python-output', (_event, data) => callback(data));
  },
  removePythonOutputListener: () => {
    ipcRenderer.removeAllListeners('python-output');
  },
});

// Type definitions for TypeScript
declare global {
  interface Window {
    electronAPI: {
      sendToPython: (data: string) => Promise<{ success: boolean; error?: string }>;
      onPythonOutput: (callback: (data: string) => void) => void;
      removePythonOutputListener: () => void;
    };
  }
}

