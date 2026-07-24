"""helpers.py — Shared utilities."""
import json
def safe_json_parse(text):
    try: return json.loads(text.replace("```json","").replace("```","").strip())
    except: return None
def truncate(s, n=200): return s[:n] + "..." if len(s) > n else s
