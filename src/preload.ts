import { contextBridge, ipcRenderer } from "electron";

contextBridge.exposeInMainWorld("api", {
  send: (txt: string) => ipcRenderer.invoke("py-in", txt),
  onOutput: (cb: (data: string) => void) =>
    ipcRenderer.on("py-out", (_event, data) => cb(data)),
});
