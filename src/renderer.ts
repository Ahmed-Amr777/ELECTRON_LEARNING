// Type declaration for api
export {};

declare global {
  interface Window {
    api: {
      send: (txt: string) => Promise<{ success: boolean; error?: string }>;
      onOutput: (cb: (data: string) => void) => void;
    };
  }
}

const inp = document.getElementById("inp") as HTMLInputElement;
const btn = document.getElementById("btn") as HTMLButtonElement;
const out = document.getElementById("out") as HTMLElement;
const clearBtn = document.getElementById("clear-btn") as HTMLButtonElement;

// Clear output
clearBtn.onclick = () => {
  out.textContent = "";
};

// Quick command buttons
document.querySelectorAll('.quick-btn').forEach(button => {
  button.addEventListener('click', () => {
    const cmd = button.getAttribute('data-cmd');
    if (cmd) {
      inp.value = cmd;
      sendCommand(cmd);
    }
  });
});

// Send command function
async function sendCommand(text: string): Promise<void> {
  if (!text.trim()) return;
  
  // Show user input
  out.textContent += `> ${text}\n`;
  out.scrollTop = out.scrollHeight;
  
  // Send to Python
  try {
    const result = await window.api.send(text);
    if (!result.success) {
      out.textContent += `[ERROR] ${result.error || "Failed to send command"}\n`;
      out.scrollTop = out.scrollHeight;
    }
  } catch (error: any) {
    out.textContent += `[ERROR] ${error.message || "Failed to send command"}\n`;
    out.scrollTop = out.scrollHeight;
  }
  inp.value = "";
}

// Main send button
btn.onclick = () => {
  const text = inp.value.trim();
  if (!text) return;
  sendCommand(text);
};

// Enter key support
inp.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    const text = inp.value.trim();
    if (text) {
      sendCommand(text);
    }
  }
});

// Listen for Python output
window.api.onOutput((txt: string) => {
  out.textContent += txt;
  out.scrollTop = out.scrollHeight;
});

// Focus input on load
window.addEventListener('load', () => {
  inp.focus();
});
