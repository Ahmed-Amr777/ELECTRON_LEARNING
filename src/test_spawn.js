const path = require('path');
const { spawn } = require('child_process');

const pythonPath = 'python'; // make sure python is on PATH
const scriptPath = path.join(__dirname, '..', 'python', 'engine.py'); // adjust based on where main.js runs

console.log('Python path:', pythonPath);
console.log('Script path:', scriptPath);

const python = spawn(pythonPath, [scriptPath]);

python.stdout.on('data', (data) => {
  console.log("Python says:", data.toString());
});

python.stderr.on('data', (data) => {
  console.error("Python error:", data.toString());
});

python.stdin.write("test line\n");
