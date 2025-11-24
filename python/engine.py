#!/usr/bin/env python3
"""
Enhanced Python Engine for Electron Application
Supports multiple command types and operations
"""

import sys
import traceback

# Import core functionality
from core import safe_print, process_command

def main():
    """Main loop with async command processing"""
    # Set stdout encoding to UTF-8 to handle Unicode characters on Windows
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except (AttributeError, ValueError):
            pass
    
    safe_print("Python Engine Ready! Type 'help' for commands.\n")
    
    try:
        for line in sys.stdin:
            if not line:
                continue
            
            # Remove trailing newline
            line = line.rstrip('\n\r')
            if not line:
                continue
            
            # Process command (async for blocking operations)
            try:
                response = process_command(line)
                if response:
                    safe_print(response)
                else:
                    # Even if no response, acknowledge command was received
                    safe_print("")
            except Exception as e:
                safe_print(f"Error processing command: {str(e)}\n{traceback.format_exc()}\n")
    
    except KeyboardInterrupt:
        safe_print("\nPython engine shutting down...\n")
    except Exception as e:
        safe_print(f"Fatal error: {str(e)}\n{traceback.format_exc()}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
