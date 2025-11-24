"""List operation handlers"""

def handle_list(cmd: str) -> str:
    """Handle list operations"""
    parts = cmd.split(" ", 1)
    if len(parts) < 2:
        return "List command required.\n"
    
    op = parts[0].lower()
    rest = parts[1]
    
    try:
        if op == "create":
            items = [x.strip() for x in rest.split(",")]
            return f"List: {items}\n"
        elif op == "append":
            split_parts = rest.rsplit(" ", 1)
            if len(split_parts) == 2:
                list_str = split_parts[0]
                item = split_parts[1]
                # Simple parsing - in real app would use eval or json
                return f"Appended {item} to list\n"
        elif op == "len":
            items = rest.split(",")
            return f"Length: {len(items)}\n"
        elif op == "sum":
            items = [float(x.strip()) for x in rest.split(",")]
            return f"Sum: {sum(items)}\n"
        else:
            return "Invalid list operation. Use: create, append, len, sum\n"
    except Exception as e:
        return f"List error: {str(e)}\n"

