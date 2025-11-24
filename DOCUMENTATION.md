# Python Engine - Electron Application Documentation

## 📋 Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Features](#features)
4. [Installation & Setup](#installation--setup)
5. [Usage Guide](#usage-guide)
6. [Python Commands Reference](#python-commands-reference)
7. [Architecture](#architecture)
8. [Development](#development)
9. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

This is an Electron desktop application that provides an interactive Python command processor. Users can execute Python commands, perform mathematical operations, manipulate strings, work with dates, and more - all through a beautiful, modern user interface.

### Key Features

- **Interactive Python Engine**: Execute Python code in real-time
- **Multiple Command Types**: Math, string operations, file operations, API calls, and more
- **Async Processing**: Long-running operations run in separate threads to prevent crashes
- **API Integration**: Make HTTP requests and receive formatted JSON responses
- **Modern UI**: Beautiful, responsive design with gradient backgrounds
- **Real-time Output**: See results instantly as you type commands
- **Quick Commands**: One-click access to common operations
- **Help System**: Built-in help command for all available operations

---

## 📁 Project Structure

```
electron_learning/
├── src/
│   ├── main.ts          # Electron main process
│   ├── preload.ts       # Preload script (IPC bridge)
│   └── renderer.ts      # Renderer process (UI logic)
├── frontend/
│   ├── index.html       # Main HTML file
│   └── style.css        # Styling
├── python/
│   ├── engine.py        # Python command processor
│   ├── requirements.txt # Python dependencies
│   └── venv/            # Python virtual environment
├── dist/                # Compiled JavaScript (generated)
├── package.json          # Node.js dependencies and scripts
├── tsconfig.main.json    # TypeScript config for main process
├── tsconfig.renderer.json # TypeScript config for renderer
└── DOCUMENTATION.md      # This file
```

---

## ✨ Features

### 1. **Basic Operations**
- Echo commands
- Evaluate Python expressions
- Execute Python code

### 2. **Mathematical Operations**
- Addition, subtraction, multiplication, division
- Power operations
- Square root
- Trigonometric functions (sin, cos)
- Mathematical constants (π, e)

### 3. **String Operations**
- Length calculation
- Case conversion (upper, lower)
- String reversal
- String splitting

### 4. **Date & Time**
- Current date
- Current time
- Full datetime

### 5. **List Operations**
- Create lists
- Calculate length
- Sum numeric lists

### 6. **Dictionary Operations**
- Create dictionaries
- Access values

### 7. **File Operations**
- Read files
- Check file existence
- Write to files

### 8. **API Operations**
- GET requests with custom headers
- POST requests with JSON data
- Formatted JSON response display
- Large JSON support with proper formatting

### 9. **Async Processing**
- Non-blocking operations for API calls, file I/O, and exec commands
- Thread-safe output handling
- Timeout protection (120 seconds)
- Prevents application crashes from long-running operations

---

## 🚀 Installation & Setup

### Prerequisites

- **Node.js** (v14 or higher)
- **npm** (comes with Node.js)
- **Python 3.x**
- **Git** (optional)

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

### Step 3: Build the Application

```bash
npm run build
```

This compiles TypeScript files to JavaScript in the `dist/` folder.

### Step 4: Run the Application

```bash
npm start
```

Or combine build and run:
```bash
npm run build && npm start
```

---

## 📖 Usage Guide

### Starting the Application

1. Run `npm start` from the project root
2. The Electron window will open automatically
3. The Python engine will start in the background
4. You'll see "Python Engine Ready! Type 'help' for commands." in the output

### Using the Interface

1. **Type a command** in the input field
2. **Click "Send"** or press **Enter**
3. **View results** in the output box below
4. **Use quick commands** for common operations
5. **Click "Clear"** to clear the output

### Example Workflow

```
1. Type: help
   Result: Shows all available commands

2. Type: eval 2 + 2
   Result: 4

3. Type: math add 10 20
   Result: 30

4. Type: str upper hello world
   Result: HELLO WORLD

5. Type: date now
   Result: 2025-01-XX
```

---

## 🐍 Python Commands Reference

### Basic Commands

| Command | Description | Example |
|---------|-------------|---------|
| `help` | Show all available commands | `help` |
| `echo <text>` | Echo back the text | `echo Hello World` |
| `eval <expression>` | Evaluate Python expression | `eval 2 + 2` |
| `exec <code>` | Execute Python code | `exec print("Hi")` |

### Math Commands

| Command | Description | Example |
|---------|-------------|---------|
| `math add <a> <b>` | Add two numbers | `math add 10 20` → 30 |
| `math sub <a> <b>` | Subtract b from a | `math sub 20 10` → 10 |
| `math mul <a> <b>` | Multiply two numbers | `math mul 5 6` → 30 |
| `math div <a> <b>` | Divide a by b | `math div 20 4` → 5.0 |
| `math pow <a> <b>` | a raised to power b | `math pow 2 8` → 256 |
| `math sqrt <n>` | Square root of n | `math sqrt 16` → 4.0 |
| `math sin <angle>` | Sine (in radians) | `math sin 1.57` → ~1.0 |
| `math cos <angle>` | Cosine (in radians) | `math cos 0` → 1.0 |
| `math pi` | Value of π | `math pi` → 3.14159... |
| `math e` | Value of e | `math e` → 2.71828... |

### String Commands

| Command | Description | Example |
|---------|-------------|---------|
| `str len <text>` | Length of string | `str len hello` → 5 |
| `str upper <text>` | Convert to uppercase | `str upper hello` → HELLO |
| `str lower <text>` | Convert to lowercase | `str lower WORLD` → world |
| `str reverse <text>` | Reverse string | `str reverse hello` → olleh |
| `str split <sep> <text>` | Split by separator | `str split , apple,banana,cherry` |

### Date/Time Commands

| Command | Description | Example |
|---------|-------------|---------|
| `date now` | Current date | `date now` → 2025-01-XX |
| `time now` | Current time | `time now` → 14:30:45 |
| `datetime now` | Current date and time | `datetime now` → 2025-01-XX 14:30:45 |

### List Commands

| Command | Description | Example |
|---------|-------------|---------|
| `list create <items>` | Create list (comma-separated) | `list create 1,2,3,4` |
| `list len <list>` | Length of list | `list len 1,2,3` → 3 |
| `list sum <list>` | Sum of numbers | `list sum 1,2,3,4` → 10 |

### Dictionary Commands

| Command | Description | Example |
|---------|-------------|---------|
| `dict create <pairs>` | Create dictionary | `dict create name:John,age:30` |

### File Commands

| Command | Description | Example |
|---------|-------------|---------|
| `file read <path>` | Read file content | `file read test.txt` |
| `file exists <path>` | Check if file exists | `file exists test.txt` |
| `file write <path> <text>` | Write text to file | `file write test.txt Hello` |

### API Commands

| Command | Description | Example |
|---------|-------------|---------|
| `api get <url>` | GET request to URL | `api get https://api.github.com/users/octocat` |
| `api post <url> [json_data]` | POST request with optional JSON | `api post https://httpbin.org/post {"name":"test"}` |
| `api get <url> headers <key:value,...>` | GET with custom headers | `api get https://api.github.com/users/octocat headers Accept:application/json` |

**API Features:**
- Automatic JSON formatting for large responses
- HTTP status code display
- Error handling for network issues
- 30-second timeout per request
- Support for custom headers

**Note:** API operations run asynchronously to prevent blocking the application.

---

## 🏗️ Architecture

### Process Communication Flow

```
┌─────────────┐
│  Renderer   │ (UI - index.html, renderer.ts)
│   Process   │
└──────┬──────┘
       │ IPC (via preload)
       ▼
┌─────────────┐
│   Preload   │ (preload.ts - Security bridge)
│    Script   │
└──────┬──────┘
       │ IPC
       ▼
┌─────────────┐      ┌──────────────┐
│    Main     │◄────►│   Python     │
│   Process   │      │   Engine     │
│  (main.ts)  │      │ (engine.py)  │
└─────────────┘      └──────────────┘
```

### How It Works

1. **User types command** in the renderer (UI)
2. **Renderer sends** command via `window.api.send()`
3. **Preload script** bridges the IPC call safely
4. **Main process** receives command via `ipcMain.handle()`
5. **Main process** writes to Python's stdin
6. **Python engine** processes command:
   - **Quick operations** (math, string, eval): Processed synchronously for instant response
   - **Blocking operations** (API, file, exec): Processed asynchronously in separate threads
7. **Python stdout** is captured by main process (thread-safe)
8. **Main process** sends output back via `webContents.send()`
9. **Renderer receives** output via `window.api.onOutput()`
10. **UI displays** the result

### Async Processing

The Python engine uses **threading** to handle potentially blocking operations:

- **Synchronous Operations**: Math, string, eval, date/time commands run instantly
- **Asynchronous Operations**: API calls, file operations, and exec commands run in separate threads
- **Thread Safety**: Output is protected with locks to prevent race conditions
- **Timeout Protection**: 120-second timeout prevents infinite blocking
- **Benefits**: 
  - No application freezing during long API calls
  - Responsive UI even during file operations
  - Prevents crashes from blocking operations

### Security Model

- **Context Isolation**: Enabled - renderer can't access Node.js directly
- **Node Integration**: Disabled - prevents security vulnerabilities
- **Preload Script**: Safely exposes only needed APIs via `contextBridge`

---

## 💻 Development

### File Descriptions

#### `src/main.ts`
- Creates Electron window
- Spawns Python process
- Handles IPC communication
- Manages application lifecycle

#### `src/preload.ts`
- Security bridge between renderer and main process
- Exposes `window.api` to renderer
- Uses `contextBridge` for safe IPC

#### `src/renderer.ts`
- UI event handlers
- Command sending logic
- Output display management
- Quick command buttons

#### `python/engine.py`
- Command processor
- Parses and executes commands
- Returns formatted results
- Handles errors gracefully

#### `frontend/index.html`
- Main UI structure
- Input form
- Output display
- Quick command buttons

#### `frontend/style.css`
- Modern, responsive styling
- Gradient backgrounds
- Dark theme output box
- Mobile-friendly design

### Building

```bash
# Build TypeScript
npm run build

# This compiles:
# - src/main.ts → dist/main.js
# - src/preload.ts → dist/preload.js
# - src/renderer.ts → dist/renderer.js
```

### Adding New Commands

To add a new Python command:

1. **Edit `python/engine.py`**:
   - Add a new `handle_*` function
   - Add command parsing in `process_command()`
   - Update `get_help()` function

2. **Example**:
```python
def handle_custom(cmd: str) -> str:
    # Your custom logic here
    return f"Result: {result}\n"

# In process_command():
if command.startswith("custom "):
    return handle_custom(command[7:])
```

---

## 🔧 Troubleshooting

### Python Not Starting

**Problem**: "Python not running" error

**Solutions**:
1. Check Python is in PATH: `python --version`
2. Or update `main.ts` to use venv Python:
   ```typescript
   const pythonPath = path.join(__dirname, "../python/venv", 
     process.platform === 'win32' ? 'Scripts' : 'bin', 
     process.platform === 'win32' ? 'python.exe' : 'python');
   py = spawn(pythonPath, [scriptPath]);
   ```

### No Output Appearing

**Problem**: Commands don't show results

**Solutions**:
1. Check DevTools console (Ctrl+Shift+I) for errors
2. Check terminal where you ran `npm start` for Python errors
3. Verify `window.api` is available in renderer
4. Make sure Python engine prints with `flush=True`

### Build Errors

**Problem**: TypeScript compilation fails

**Solutions**:
1. Run `npm run build` to see detailed errors
2. Check `tsconfig.main.json` and `tsconfig.renderer.json` exist
3. Verify all imports are correct

### File Operations Not Working

**Problem**: File commands fail

**Solutions**:
1. Use absolute paths or paths relative to Python working directory
2. Check file permissions
3. Verify file exists before reading

### API Operations Not Working

**Problem**: API commands fail or timeout

**Solutions**:
1. Ensure `requests` library is installed: `pip install requests`
2. Check internet connection
3. Verify URL is correct and accessible
4. Check if API requires authentication (use headers)
5. Large responses are truncated to 5000 characters for display

### Application Freezing

**Problem**: App becomes unresponsive during operations

**Solutions**:
1. This should not happen with async operations - check if command is in `async_commands` list
2. Operations have 120-second timeout - if exceeded, command will fail gracefully
3. Check Python process logs for errors
4. Restart the application if it becomes unresponsive

---

## 📝 Examples

### Example Session

```
> help
=== Python Engine Commands ===
[Shows all commands...]

> eval 2 + 2
Result: 4

> math add 15 25
Result: 40.0

> math sqrt 144
Result: 12.0

> str upper hello world
Result: HELLO WORLD

> str reverse python
Result: nohtyp

> date now
Date: 2025-01-15

> time now
Time: 14:30:45

> list sum 1,2,3,4,5
Sum: 15.0

> exec print("Hello from Python!")
Hello from Python!
Code executed successfully
```

---

## 🎨 UI Features

### Design Elements

- **Gradient Header**: Purple gradient background
- **Dark Output Box**: Terminal-style dark theme
- **Quick Commands**: One-click access to common operations
- **Responsive Design**: Works on different screen sizes
- **Smooth Animations**: Hover effects and transitions
- **Command Reference**: Expandable help section

### Keyboard Shortcuts

- **Enter**: Send command
- **Tab**: Focus input field (when available)

---

## 📦 Building for Distribution

### Creating an Executable

1. Install electron-builder:
```bash
npm install --save-dev electron-builder
```

2. Add to `package.json`:
```json
{
  "build": {
    "appId": "com.example.pythonengine",
    "productName": "Python Engine",
    "directories": {
      "output": "release"
    },
    "files": [
      "dist/**/*",
      "frontend/**/*",
      "python/**/*",
      "package.json"
    ],
    "win": {
      "target": "nsis"
    }
  },
  "scripts": {
    "dist": "npm run build && electron-builder"
  }
}
```

3. Build:
```bash
npm run dist
```

---

## 🔐 Security Notes

- The application uses Electron's security best practices
- Context isolation prevents direct Node.js access from renderer
- Only necessary APIs are exposed via preload script
- Python code execution is sandboxed to the engine process
- API requests have 30-second timeout to prevent hanging
- Async processing prevents blocking operations from crashing the app

---

## 📄 License

ISC

---

## 🤝 Contributing

To extend this application:

1. Add new command handlers in `python/engine.py`
2. Update the help text
3. Add UI elements if needed in `frontend/index.html`
4. Update this documentation

---

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Review the code comments
- Check DevTools console for errors
- Verify Python environment setup

---

**Last Updated**: January 2025
**Version**: 1.0.0

