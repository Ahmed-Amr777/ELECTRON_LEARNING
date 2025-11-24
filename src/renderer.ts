// Renderer process code
// This file can be used for any client-side TypeScript code

document.addEventListener('DOMContentLoaded', () => {
  console.log('Renderer process loaded');

  // Set up Python output listener
  if (window.electronAPI) {
    window.electronAPI.onPythonOutput((data: string) => {
      const outputDiv = document.getElementById('python-output');
      if (outputDiv) {
        outputDiv.textContent += data;
        outputDiv.scrollTop = outputDiv.scrollHeight;
      }
    });
  }

  // Handle form submission
  const form = document.getElementById('python-form') as HTMLFormElement;
  const input = document.getElementById('python-input') as HTMLInputElement;

  if (form && input && window.electronAPI) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const value = input.value.trim();
      if (value) {
        const result = await window.electronAPI.sendToPython(value);
        if (result.success) {
          input.value = '';
        } else {
          console.error('Failed to send to Python:', result.error);
        }
      }
    });
  }
});

