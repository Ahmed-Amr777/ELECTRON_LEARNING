"""API operation handlers"""
import json
import traceback

# Try to import requests
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

def handle_api(cmd: str) -> str:
    """Handle API requests"""
    if not HAS_REQUESTS:
        return "Error: 'requests' library not installed. Run: pip install requests\n"
    
    try:
        parts = cmd.split(" ", 1)
        if len(parts) < 2:
            return "Usage: api get <url> or api post <url> [json_data]\n"
        
        method = parts[0].upper()
        rest = parts[1].strip()
        
        if method == "GET":
            # Check for headers
            if " headers " in rest:
                url_part, headers_part = rest.split(" headers ", 1)
                url = url_part.strip()
                headers = {}
                for pair in headers_part.split(","):
                    if ":" in pair:
                        k, v = pair.split(":", 1)
                        headers[k.strip()] = v.strip()
                
                response = requests.get(url, headers=headers, timeout=30)
            else:
                url = rest
                response = requests.get(url, timeout=30)
            
            # Format JSON response nicely
            try:
                json_data = response.json()
                formatted_json = json.dumps(json_data, indent=2, ensure_ascii=False)
                return f"Status: {response.status_code}\nURL: {url}\n\nJSON Response:\n{formatted_json}\n"
            except ValueError:
                # Not JSON, return as text
                return f"Status: {response.status_code}\nURL: {url}\n\nResponse:\n{response.text[:5000]}\n"
        
        elif method == "POST":
            # Parse URL and optional JSON data
            if " " in rest:
                url, json_str = rest.split(" ", 1)
                url = url.strip()
                try:
                    json_data = json.loads(json_str)
                    response = requests.post(url, json=json_data, timeout=30)
                except json.JSONDecodeError:
                    # If not valid JSON, send as data
                    response = requests.post(url, data=json_str, timeout=30)
            else:
                url = rest
                response = requests.post(url, timeout=30)
            
            # Format JSON response nicely
            try:
                json_data = response.json()
                formatted_json = json.dumps(json_data, indent=2, ensure_ascii=False)
                return f"Status: {response.status_code}\nURL: {url}\n\nJSON Response:\n{formatted_json}\n"
            except ValueError:
                return f"Status: {response.status_code}\nURL: {url}\n\nResponse:\n{response.text[:5000]}\n"
        
        else:
            return f"Unsupported method: {method}. Use GET or POST.\n"
    
    except requests.exceptions.RequestException as e:
        return f"API Error: {str(e)}\n"
    except Exception as e:
        return f"Error: {str(e)}\n{traceback.format_exc()}\n"

