#!/usr/bin/env python3
"""
Python Engine for Electron Application
Handles communication with the Electron main process via stdin/stdout
"""

import sys
import json
import traceback

def process_command(command: str) -> str:
    """
    Process a command received from Electron and return a response.
    
    Args:
        command: The command string received from stdin
        
    Returns:
        A response string to send back
    """
    try:
        command = command.strip()
        
        # Example: Echo command
        if command.startswith('echo '):
            print(f"Echo: {command[5:]}")
            return f"Echo: {command[5:]}\n"
        
        # Example: Evaluate Python expression
        elif command.startswith('eval '):
            try:
                expr = command[5:]
                result = eval(expr)
                return f"Result: {result}\n"
            except Exception as e:
                return f"Error: {str(e)}\n"
        
        # Example: Execute Python code
        elif command.startswith('exec '):
            try:
                code = command[5:]
                exec(code)
                return "Code executed successfully\n"
            except Exception as e:
                return f"Error: {str(e)}\n"
        
        # Default: Just echo back
        else:
            return f"Received: {command}\n"
    
    except Exception as e:
        return f"Error processing command: {str(e)}\n{traceback.format_exc()}\n"

def main():
    """Main loop to read from stdin and write to stdout"""
    print("Python engine started. Ready to receive commands.", flush=True)
    
    try:
        while True:
            # Read from stdin
            line = sys.stdin.readline()
            
            if not line:
                break
            
            # Process the command
            response = process_command(line)
            
            # Write response to stdout
            print(response, end='', flush=True)
    
    except KeyboardInterrupt:
        print("\nPython engine shutting down...", flush=True)
    except Exception as e:
        print(f"Fatal error: {str(e)}\n{traceback.format_exc()}", flush=True)
        sys.exit(1)

if __name__ == '__main__':
    main()

