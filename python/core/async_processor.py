"""Async command processing"""
import threading
from queue import Queue
from typing import Dict, Callable

from .output import safe_print

# Import handlers - using absolute import from python package
try:
    from handlers import (
        handle_basic, handle_math, handle_string, handle_datetime,
        handle_list, handle_dict, handle_file, handle_api, handle_exec, handle_eval
    )
except ImportError:
    # Fallback: add parent directory to path
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from handlers import (
        handle_basic, handle_math, handle_string, handle_datetime,
        handle_list, handle_dict, handle_file, handle_api, handle_exec, handle_eval
    )

def process_command_sync(command: str) -> str:
    """Process commands synchronously (for quick operations)"""
    import traceback
    
    try:
        command = command.strip()
        if not command:
            return ""
        
        # Test command
        if command == "test":
            return handle_basic("test")
        
        # Help command
        if command == "help" or command == "?":
            return handle_basic("help")
        
        # Math operations
        if command.startswith("math "):
            return handle_math(command[5:])
        
        # String operations
        if command.startswith("str "):
            return handle_string(command[4:])
        
        # Date/Time operations
        if command.startswith("date") or command.startswith("time"):
            return handle_datetime(command)
        
        # List operations
        if command.startswith("list "):
            return handle_list(command[5:])
        
        # Dictionary operations
        if command.startswith("dict "):
            return handle_dict(command[5:])
        
        # Echo command
        if command.startswith("echo "):
            return handle_basic("echo", command[5:])
        
        # Evaluate Python expression (with or without space)
        if command.startswith("eval "):
            return handle_eval(command[5:])
        elif command.startswith("eval"):
            # Handle "eval2+2" or "eval(2+2)" cases
            rest = command[4:].strip()
            if rest:
                return handle_eval(rest)
            else:
                return "Usage: eval <expression>\nExample: eval 2+2\n"
        
        # Default: try to evaluate as expression (for simple math like "2+2")
        try:
            # Only try eval if it looks like a simple expression (no spaces or common operators)
            if any(op in command for op in ['+', '-', '*', '/', '**', '(', ')', '%', '//']):
                result = eval(command)
                return f"Result: {result}\n"
            else:
                return f"Unknown command: {command}\nType 'help' for available commands.\n"
        except:
            return f"Unknown command: {command}\nType 'help' for available commands.\n"
    
    except Exception as e:
        return f"Error: {str(e)}\n{traceback.format_exc()}\n"

def process_command_async(command: str, result_queue: Queue):
    """Process command asynchronously and put result in queue"""
    import traceback
    
    try:
        command = command.strip()
        
        # Handle async operations directly
        if command.startswith("file "):
            result = handle_file(command[5:])
        # API operations
        elif command.startswith("api "):
            result = handle_api(command[4:])
        # Execute Python code
        elif command.startswith("exec "):
            result = handle_exec(command[5:])
        else:
            # Fallback to sync processing for other commands
            result = process_command_sync(command)
        
        result_queue.put(result)
    except Exception as e:
        result_queue.put(f"Error: {str(e)}\n{traceback.format_exc()}\n")

def process_command(command: str) -> str:
    """Process commands - routes to sync or async based on operation type"""
    command = command.strip()
    if not command:
        return ""
    
    # Operations that should run asynchronously (potentially blocking)
    async_commands = ["api ", "file ", "exec "]
    
    # Check if this is a blocking operation
    is_async = any(command.startswith(cmd) for cmd in async_commands)
    
    if is_async:
        # Run in a separate thread to avoid blocking
        result_queue = Queue()
        thread = threading.Thread(target=process_command_async, args=(command, result_queue))
        thread.daemon = True
        thread.start()
        
        # Wait for result with timeout (prevents infinite blocking)
        try:
            result = result_queue.get(timeout=120)  # 120 second timeout for long operations
            return result
        except:
            thread.join(timeout=1)  # Try to cleanup
            return "Error: Operation timed out (exceeded 120 seconds)\n"
    else:
        # Quick operations run synchronously
        return process_command_sync(command)

