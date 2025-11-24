"""Date/time operation handlers"""
import datetime

def handle_datetime(cmd: str) -> str:
    """Handle date/time operations"""
    now = datetime.datetime.now()
    
    if cmd == "date now":
        return f"Date: {now.strftime('%Y-%m-%d')}\n"
    elif cmd == "time now":
        return f"Time: {now.strftime('%H:%M:%S')}\n"
    elif cmd == "datetime now" or cmd == "now":
        return f"DateTime: {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
    else:
        return "Use: 'date now', 'time now', or 'datetime now'\n"

