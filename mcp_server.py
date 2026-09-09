import sys
import json
from client import VRReplica

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "test_view_change":
        r = VRReplica(0, 3)
        return r.start_view_change()
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
