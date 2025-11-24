"""Math operation handlers"""
import math

def handle_math(cmd: str) -> str:
    """Handle math operations"""
    parts = cmd.split()
    if not parts:
        return "Math command required. Use 'math add <a> <b>', etc.\n"
    
    op = parts[0].lower()
    
    try:
        if op == "add" and len(parts) == 3:
            result = float(parts[1]) + float(parts[2])
            return f"Result: {result}\n"
        elif op == "sub" and len(parts) == 3:
            result = float(parts[1]) - float(parts[2])
            return f"Result: {result}\n"
        elif op == "mul" and len(parts) == 3:
            result = float(parts[1]) * float(parts[2])
            return f"Result: {result}\n"
        elif op == "div" and len(parts) == 3:
            result = float(parts[1]) / float(parts[2])
            return f"Result: {result}\n"
        elif op == "pow" and len(parts) == 3:
            result = float(parts[1]) ** float(parts[2])
            return f"Result: {result}\n"
        elif op == "sqrt" and len(parts) == 2:
            result = math.sqrt(float(parts[1]))
            return f"Result: {result}\n"
        elif op == "sin" and len(parts) == 2:
            result = math.sin(float(parts[1]))
            return f"Result: {result}\n"
        elif op == "cos" and len(parts) == 2:
            result = math.cos(float(parts[1]))
            return f"Result: {result}\n"
        elif op == "pi":
            return f"pi = {math.pi}\n"
        elif op == "e":
            return f"e = {math.e}\n"
        else:
            return "Invalid math operation. Use: add, sub, mul, div, pow, sqrt, sin, cos, pi, e\n"
    except Exception as e:
        return f"Math error: {str(e)}\n"

