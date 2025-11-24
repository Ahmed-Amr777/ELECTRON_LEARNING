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
│   ├─ engine.py         # Entry point that wires everything together
│   ├─ core/             # Core utilities (async routing, output helpers)
│   │   ├─ async_processor.py
│   │   └─ output.py
│   ├─ handlers/         # Individual command handlers
│   │   ├─ basic.py      # help / test / echo
│   │   ├─ math.py       # all math_operations
│   │   ├─ string.py     # string tools
│   │   ├─ datetime.py   # date/time helpers
│   │   ├─ list.py
│   │   ├─ dict.py
│   │   ├─ file.py       # file read/write/exists (async)
│   │   ├─ api.py        # HTTP GET/POST (async)
│   │   └─ exec.py       # eval / exec helpers
│   ├─ requirements.txt  # Python dependencies (requests, etc.)
│   └─ venv/             # Python virtual environment (not in git)
└─ dist/             # Compiled JavaScript (generated)
```

## Prerequisites

- **Node.js** (v14 or higher) and npm installed
- **Python 3.x** installed
- **Git** (optional, for cloning)

## Setup Instructions

### Step 1: Install Node.js Dependencies

```bash
npm install
```

This installs:
- Electron
- TypeScript
- Type definitions

### Step 2: Set Up Python Virtual Environment

**Windows:**
```bash
cd python
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
cd python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Note:** The virtual environment (`venv/`) is already in `.gitignore`, so you need to create it locally. The `requirements.txt` installs `requests`, which powers the API commands—make sure the install succeeds.

### Step 3: Verify Setup

Make sure:
- ✅ `node_modules/` folder exists (from `npm install`)
- ✅ `python/venv/` folder exists (from `python -m venv venv`)
- ✅ Python packages are installed (from `pip install -r requirements.txt`)

## Running the Application

### Quick Start (Recommended)

```bash
npm start
```

This command will:
1. Compile TypeScript files to JavaScript in the `dist/` folder
2. Launch the Electron application

### Manual Build and Run

If you prefer to build separately:

```bash
# Build TypeScript
npm run build

# Then run Electron
npx electron .
```

## Usage

1. **Launch the app**: Run `npm start`
2. **Electron window opens**: The application window will appear automatically
3. **Python engine starts**: The Python backend starts in the background
4. **Send commands**: Type commands in the input field:
   - `echo Hello World` - Echo back the message
   - `eval 2 + 2` - Evaluate a Python expression (result: 4)
   - `exec print("Hello from Python")` - Execute Python code
   - Or any other text to see it processed
5. **View output**: See the results in the output box below

### Python Engine Architecture

The Python backend is modular and organized into focused components:

#### Module Structure

```
python/
├── engine.py              # Main entry point (stdin/stdout loop)
├── core/
│   ├── async_processor.py # Command router & async handler
│   └── output.py         # Thread-safe output with encoding fixes
└── handlers/
    ├── basic.py          # test, help, echo
    ├── math.py           # Math operations
    ├── string.py         # String operations
    ├── datetime.py       # Date/time operations
    ├── list.py           # List operations
    ├── dict.py           # Dictionary operations
    ├── file.py           # File I/O (async)
    ├── api.py            # HTTP requests (async)
    └── exec.py           # Code execution (async)
```

#### Command Flow Architecture

```
┌─────────────┐
│  Renderer   │ (UI - frontend/index.html, src/renderer.ts)
│   Process   │
└──────┬──────┘
       │ IPC (via preload)
       ▼
┌─────────────┐
│   Preload   │ (src/preload.ts - Security bridge)
│    Script   │
└──────┬──────┘
       │ IPC
       ▼
┌─────────────┐      ┌──────────────────────────┐
│    Main     │─────►│   python/engine.py       │
│   Process   │      │   (Main Entry Point)     │
│  (main.ts)  │      └───────────┬──────────────┘
└─────────────┘                  │
                                  │ stdin/stdout
                                  ▼
                    ┌─────────────────────────────┐
                    │ core/async_processor.py     │
                    │ (Command Router)            │
                    └───────┬─────────────────────┘
                            │
        ┌───────────────────┴───────────────────┐
        │                                         │
        ▼                                         ▼
┌──────────────────┐                  ┌──────────────────┐
│  Quick Commands   │                  │  Blocking Commands│
│  (Synchronous)    │                  │  (Asynchronous)    │
├──────────────────┤                  ├──────────────────┤
│ • math           │                  │ • api            │
│ • string         │                  │ • file           │
│ • datetime       │                  │ • exec           │
│ • list           │                  │                  │
│ • dict           │                  │ Runs in thread   │
│ • eval           │                  │ with 120s timeout│
│ • echo           │                  │                  │
│ • test           │                  │                  │
└──────────────────┘                  └──────────────────┘
        │                                         │
        └───────────────────┬───────────────────┘
                            │
                            ▼
                    ┌──────────────────┐
                    │ core/output.py   │
                    │ (Thread-safe)    │
                    └──────────────────┘
                            │
                            ▼
                    ┌──────────────────┐
                    │  stdout → UI     │
                    └──────────────────┘
```

#### Key Features

- **Modular Design**: Each command type in its own handler file
- **Async Processing**: Blocking operations (API, file, exec) run in separate threads
- **Thread Safety**: Output protected with locks to prevent race conditions
- **Timeout Protection**: 120-second timeout prevents infinite blocking
- **Encoding Support**: Handles Windows Unicode encoding issues gracefully

**Async Operations:** Commands like `api`, `file`, and `exec` are processed in background threads with a 120-second timeout, ensuring the Electron UI never freezes during long operations.

## Development

### Making Changes

- **TypeScript files**: Edit files in `src/`, then run `npm run build`
- **Frontend files**: Edit `frontend/index.html` or `frontend/style.css` (no rebuild needed)
- **Python engine**:
  - Quick tweaks: edit the corresponding file in `python/handlers/`
  - Core behavior/timeouts: edit `python/core/async_processor.py`
  - Entry point / stdout handling: edit `python/engine.py`
  - Restart Electron after Python changes to reload the child process

### Rebuilding After Changes

```bash
npm run build
```

Then restart the app with `npm start`.

## Troubleshooting

### Python Not Found
- **Issue**: "Python process not available" error
- **Solution**: 
  1. Make sure you created the virtual environment: `python -m venv python/venv`
  2. Verify the path: Check that `python/venv/Scripts/python.exe` exists (Windows) or `python/venv/bin/python` exists (Linux/Mac)

### Build Errors
- **Issue**: TypeScript compilation fails
- **Solution**: Run `npm run build` to see detailed error messages

### Window Doesn't Open
- **Issue**: No window appears when running `npm start`
- **Solution**: 
  1. Check console for error messages
  2. Verify `dist/main.js` exists (run `npm run build` first)
  3. Check that `frontend/index.html` exists

### Python Packages Not Found
- **Issue**: Python errors about missing modules
- **Solution**: 
  1. Activate virtual environment: `python\venv\Scripts\activate` (Windows) or `source python/venv/bin/activate` (Linux/Mac)
  2. Install requirements: `pip install -r python/requirements.txt`

### Dependencies Not Installed
- **Issue**: `npm install` fails or `node_modules` missing
- **Solution**: 
  1. Delete `node_modules` folder (if exists)
  2. Delete `package-lock.json` (if exists)
  3. Run `npm install` again

## Project Commands Summary

```bash
# Install Node.js dependencies
npm install

# Create Python virtual environment (Windows)
cd python && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

# Create Python virtual environment (Linux/Mac)
cd python && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Build TypeScript
npm run build

# Run the application
npm start
```

## License

ISC
