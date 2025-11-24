"""Code execution handlers"""
import traceback

def handle_exec(code: str) -> str:
    """Execute Python code"""
    try:
        exec(code)
        return "Code executed successfully\n"
    except Exception as e:
        return f"Execution error: {str(e)}\n{traceback.format_exc()}\n"

def handle_eval(expr: str) -> str:
    """Evaluate Python expression"""
    try:
        result = eval(expr)
        return f"Result: {result}\n"
    except Exception as e:
        return f"Evaluation error: {str(e)}\n"

