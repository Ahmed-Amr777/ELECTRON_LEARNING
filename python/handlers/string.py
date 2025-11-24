"""String operation handlers"""

def handle_string(cmd: str) -> str:
    """Handle string operations"""
    parts = cmd.split(" ", 1)
    if len(parts) < 2:
        return "String command required. Use 'str len <text>', etc.\n"
    
    op = parts[0].lower()
    text = parts[1]
    
    try:
        if op == "len":
            return f"Length: {len(text)}\n"
        elif op == "upper":
            return f"Result: {text.upper()}\n"
        elif op == "lower":
            return f"Result: {text.lower()}\n"
        elif op == "reverse":
            return f"Result: {text[::-1]}\n"
        elif op == "split":
            split_parts = text.split(" ", 1)
            if len(split_parts) == 2:
                sep = split_parts[0]
                txt = split_parts[1]
                result = txt.split(sep)
                return f"Result: {result}\n"
            else:
                return "Usage: str split <separator> <text>\n"
        else:
            return "Invalid string operation. Use: len, upper, lower, reverse, split\n"
    except Exception as e:
        return f"String error: {str(e)}\n"

