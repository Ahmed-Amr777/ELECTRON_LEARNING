"""Basic command handlers (test, help, echo)"""
import traceback

def get_help() -> str:
    """Return help message"""
    return """
=== Python Engine Commands ===

BASIC:
  test                     - Test if Python engine is working
  echo <text>              - Echo back text
  eval <expression>        - Evaluate Python expression
  exec <code>              - Execute Python code (async)
  help                     - Show this help

MATH:
  math add <a> <b>         - Add two numbers
  math sub <a> <b>         - Subtract b from a
  math mul <a> <b>         - Multiply two numbers
  math div <a> <b>         - Divide a by b
  math pow <a> <b>         - a raised to power b
  math sqrt <n>            - Square root of n
  math sin <angle>         - Sine (radians)
  math cos <angle>         - Cosine (radians)
  math pi                  - Value of pi
  math e                   - Value of e

STRING:
  str len <text>           - Length of string
  str upper <text>         - Convert to uppercase
  str lower <text>         - Convert to lowercase
  str reverse <text>       - Reverse string
  str split <sep> <text>   - Split string by separator

DATE/TIME:
  date now                 - Current date
  time now                 - Current time
  datetime now             - Current date and time

LIST:
  list create <items>      - Create list from items (comma-separated)
  list len <items>         - Length of list
  list sum <items>         - Sum of numbers in list

DICT:
  dict create <key1:val1,key2:val2> - Create dictionary

FILE (async):
  file read <path>          - Read file content
  file exists <path>        - Check if file exists
  file write <path> <text>  - Write text to file

API (async):
  api get <url>             - GET request to URL
  api post <url> [json]     - POST request with optional JSON data
  api get <url> headers <key:value,...> - GET with custom headers

NOTES:
  - Commands marked (async) run in separate threads to prevent blocking
  - API operations have 30-second timeout
  - File operations have 120-second timeout
  - Large JSON responses are automatically formatted

EXAMPLES:
  test
  eval 2 + 2
  math add 10 20
  str upper hello world
  date now
  api get https://api.github.com/users/octocat
  api post https://httpbin.org/post {"name":"test","value":123}
  file read test.txt
"""

def handle_basic(cmd: str, *args) -> str:
    """Handle basic commands"""
    if cmd == "test":
        return "Python engine is working!\n"
    elif cmd == "help" or cmd == "?":
        return get_help()
    elif cmd == "echo":
        if args:
            return f"Echo: {args[0]}\n"
        return "Usage: echo <text>\n"
    else:
        return f"Unknown basic command: {cmd}\n"

