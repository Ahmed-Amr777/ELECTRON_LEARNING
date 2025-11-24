"""File operation handlers"""
import os

def handle_file(cmd: str) -> str:
    """Handle file operations"""
    parts = cmd.split(" ", 1)
    if len(parts) < 2:
        return "File command required.\n"
    
    op = parts[0].lower()
    rest = parts[1]
    
    try:
        if op == "read":
            with open(rest, 'r', encoding='utf-8') as f:
                content = f.read()
            return f"File content:\n{content}\n"
        elif op == "exists":
            exists = os.path.exists(rest)
            return f"File exists: {exists}\n"
        elif op == "write":
            write_parts = rest.split(" ", 1)
            if len(write_parts) == 2:
                path = write_parts[0]
                content = write_parts[1]
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return f"File written: {path}\n"
            else:
                return "Usage: file write <path> <content>\n"
        else:
            return "Invalid file operation. Use: read, exists, write\n"
    except Exception as e:
        return f"File error: {str(e)}\n"

