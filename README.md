# Electron Learning Project

An Electron application with Python integration for learning purposes.

## Project Structure

```
├─ src/              # TypeScript source files
│   ├─ main.ts       # Main Electron process
│   ├─ preload.ts    # Preload script (bridge)
│   └─ renderer.ts   # Renderer process code
├─ frontend/         # Frontend files
│   ├─ index.html    # Main HTML file
│   └─ style.css     # Styles
├─ python/           # Python backend
│   ├─ engine.py     # Python engine
│   └─ venv/         # Python virtual environment
└─ dist/             # Compiled JavaScript (generated)
```

## Prerequisites

- Node.js and npm installed
- Python 3.x installed
- Python virtual environment set up in `python/venv/`

## Setup

1. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

2. **Ensure Python virtual environment is activated:**
   - Windows: `python\venv\Scripts\activate`
   - Linux/Mac: `source python/venv/bin/activate`

## Running the Application

### Option 1: Build and Run (Recommended)
```bash
npm start
```

This will:
1. Compile TypeScript files to JavaScript in the `dist/` folder
2. Launch the Electron application

### Option 2: Build Separately
```bash
# Build TypeScript
npm run build

# Then run Electron
npx electron .
```

## Usage

1. The Electron window will open automatically
2. The Python engine will start in the background
3. Type commands in the input field:
   - `echo Hello World` - Echo back the message
   - `eval 2 + 2` - Evaluate a Python expression
   - `exec print("Hello from Python")` - Execute Python code
   - Or any other text to see it echoed back
4. View the output in the output box below

## Development

- Edit TypeScript files in `src/`
- Edit frontend files in `frontend/`
- Edit Python engine in `python/engine.py`
- Rebuild after changes: `npm run build`

## Troubleshooting

- **Python not found**: Make sure the virtual environment is set up correctly
- **Build errors**: Run `npm run build` to see TypeScript errors
- **Window doesn't open**: Check the console for error messages

