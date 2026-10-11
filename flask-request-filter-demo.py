from urllib.parse import unquote
import re
from flask import Flask, request, abort

app = Flask(__name__)

# define WAF rules (regular expression for common attack payloads)
WAF_RULES = {
    "SQL_Injection": re.compile(
        r"UNION\s+SELECT\s+.*\s+FROM|OR\s+\d+=\d+|'--|--",
        re.IGNORECASE
    ),
    "Cross_Site_Scripting_XSS": re.compile(
        r"<script\b[^>]*>.*?</script\s*>|javascript:|onerror\s*=|onload\s*=",
        re.IGNORECASE
    ),
    "Path_Traversal": re.compile(
        r"(?:\.\./|\.\.\\)+|etc/passwd",
        re.IGNORECASE
    )
}

# global request inspection middleware
@app.before_request
def inspect_incoming_request():
    """
    Scans query strings, URL paths, and form/JSON bodies for malicious patterns.
    """
    # gather strings to inspect
    payloads_to_check = [
        unquote(request.path),
        unquote(request.query_string.decode('utf-8', errors='ignore'))
    ]

    # extract data from request bodies if available
    if request.form:
        payloads_to_check.extend(request.form.values())
    if request.is_json:
        # flatten dictionary values to a list of strings
        json_data = request.get_json(silent=True)
        if isinstance(json_data, dict):
            payloads_to_check.extend(str(v) for v in json_data.values())

    # match payloads against rules
    for payload in payloads_to_check:
        if not payload:
            continue
        for attack_name, pattern in WAF_RULES.items():
            if pattern.search(payload):
               # send 403 forbidden alert
               app.logger.warning(f"WAF Blocked Request! Attack Type: {attack_name} | Payload: {payload}")
               abort(403, description=f"Access Denied: Malicious activity detected ({attack_name}).")

# protected application routes
@app.route('/')
def home():
    return {"status": "Success", "message": "Welcome! Your Request safely passed through the WAF."}

@app.route('/submit', methods=['POST'])
def submit():
    return {"status": "Success", "message": "Data processed securely."}

if __name__ == '__main__':
    # run server locally
    app.run(host='127.0.0.1', port=5000, debug=True)                            
