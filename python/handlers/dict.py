"""Dictionary operation handlers"""

def handle_dict(cmd: str) -> str:
    """Handle dictionary operations"""
    parts = cmd.split(" ", 1)
    if len(parts) < 2:
        return "Dict command required.\n"
    
    op = parts[0].lower()
    rest = parts[1]
    
    try:
        if op == "create":
            # Simple parsing: key1:val1,key2:val2
            pairs = rest.split(",")
            result = {}
            for pair in pairs:
                if ":" in pair:
                    k, v = pair.split(":", 1)
                    result[k.strip()] = v.strip()
            return f"Dict: {result}\n"
        else:
            return "Dict operations: create\n"
    except Exception as e:
        return f"Dict error: {str(e)}\n"

