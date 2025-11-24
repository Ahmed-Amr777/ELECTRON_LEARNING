"""Thread-safe output handling"""
import threading

# Thread-safe output lock
output_lock = threading.Lock()

def safe_print(text: str):
    """Thread-safe print function with encoding error handling"""
    with output_lock:
        try:
            print(text, end='', flush=True)
        except UnicodeEncodeError:
            # Handle encoding errors on Windows (cp1252 can't encode some Unicode chars)
            try:
                # Try UTF-8 encoding
                encoded = text.encode('utf-8', errors='replace').decode('utf-8', errors='replace')
                print(encoded, end='', flush=True)
            except:
                # Fallback: replace non-ASCII characters
                safe_text = text.encode('ascii', errors='replace').decode('ascii')
                print(safe_text, end='', flush=True)

