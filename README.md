# Python Mini Projects

Small Python and cybersecurity learning projects. This guide explains what each script does, what it demonstrates, and how to run it.

## Projects

| Script | Purpose and possible use | Learning focus |
|---|---|---|
| [dns-lookup-tool.py](dns-lookup-tool.py) | Looks up a domain's IP address and reverse hostname. | DNS, sockets, and network errors |
| [common-tcp-port-scanner.py](common-tcp-port-scanner.py) | Checks a short list of TCP ports on a host you own or are authorized to assess. | TCP connections, ports, and timeouts |
| [password-strength-checker.py](password-strength-checker.py) | Gives feedback based on basic password length and character checks. | Input validation, regular expressions, and password policy |
| [caesar-cipher-encryptor.py](caesar-cipher-encryptor.py) | Shifts letters by a chosen amount while preserving other characters. | Character codes, loops, and modular arithmetic; this is not secure encryption |
| [suspicious-url-checker.py](suspicious-url-checker.py) | Flags a few URL patterns for review. | String checks and simple security heuristics; this is not a reliable phishing detector |
| [bcrypt-password-login-demo.py](bcrypt-password-login-demo.py) | Demonstrates hashing a password and checking a login attempt. | Salted password hashing and verification |
| [ip-geolocation-lookup.py](ip-geolocation-lookup.py) | Requests approximate location and ISP details for an IP from an external service. | HTTP requests, JSON, and data privacy |
| [sha256-file-hash-checker.py](sha256-file-hash-checker.py) | Calculates a file's SHA-256 checksum. | Cryptographic hashes and chunked file reading |
| [firewall-rule-simulator.py](firewall-rule-simulator.py) | Adds and checks blocked IPs in memory; it does not change system firewall settings. | Lists, conditions, and access-control logic |
| [three-letter-password-guessing-demo.py](three-letter-password-guessing-demo.py) | Demonstrates a hard-coded three-letter guessing loop against a toy example. | Nested loops and the scale of brute-force search; local learning demo only |
| [timed-otp-demo.py](timed-otp-demo.py) | Generates a six-digit code and checks it against a time limit. | Random values and time checks; the code is displayed in the same terminal, so this is not real authentication |
| [keystroke-logger-demo.py](keystroke-logger-demo.py) | Demonstrates keyboard event logging with active-window labels. | Event listeners and file handling; it records sensitive input, so only run on your own device with informed consent |
| [reflected-xss-form-checker-lab.py](reflected-xss-form-checker-lab.py) | Demonstrates basic reflected-XSS checks against web forms. | HTML form parsing, HTTP methods, and reflected input; its target is hard-coded, so do not run it unchanged or against a site without explicit authorization |
| [sql-error-signature-checker-lab.py](sql-error-signature-checker-lab.py) | Demonstrates checking a response for common database error text. | HTTP requests and response inspection; its target is hard-coded, so do not run it unchanged or against a site without explicit authorization |
| [flask-request-filter-demo.py](flask-request-filter-demo.py) | Runs a small local Flask app that blocks requests matching illustrative rules. | Middleware, regular expressions, and HTTP responses; not a production WAF |
| [jwt-security-analyzer-demo.py](jwt-security-analyzer-demo.py) | Decodes JWT metadata and flags selected claims and algorithms. | JWT structure and token claims; it does not verify signatures or prove a token is secure |
| [http-packet-sniffer-demo.py](http-packet-sniffer-demo.py) | Demonstrates viewing TCP traffic on port 80 with Scapy. | Packet capture and TCP/IP; packet contents can be sensitive, so only capture on a network you own or are authorized to monitor |
| [md5-file-signature-scanner-demo.py](md5-file-signature-scanner-demo.py) | Compares file MD5 hashes with a tiny sample list. | File walking, hashing, and signature matching; not a production malware scanner |
| [flask-login-rate-limiter-demo.py](flask-login-rate-limiter-demo.py) | Demonstrates a Flask login endpoint with IP rate limits and temporary in-memory lockouts. | API routes, rate limiting, and mock authentication; not production authentication |
| [fastapi-jwt-role-access-demo.py](fastapi-jwt-role-access-demo.py) | Demonstrates a FastAPI login flow with JWTs and role-checked routes using mock users. | API schemas, tokens, and role-based access control; demo credentials are not for real accounts |
| [wordlist-hash-checker-demo.py](wordlist-hash-checker-demo.py) | Checks a supplied wordlist against a hash you are authorized to audit. | Hash algorithms, file input, and dictionary-based auditing; use only with hashes you own or have permission to assess |

## How to run

Install Python 3, clone or download this repository, open Command Prompt in the repository folder, and run a script:

```cmd
py dns-lookup-tool.py
```

Replace the filename with the script you want. If `py` is unavailable, try `python` instead. Most scripts use Python's standard library.

### Extra packages

Install only the packages needed for the script you want to run:

| Script(s) | Command Prompt install command |
|---|---|
| `ip-geolocation-lookup.py`, `sql-error-signature-checker-lab.py` | `py -m pip install requests` |
| `reflected-xss-form-checker-lab.py` | `py -m pip install requests beautifulsoup4` |
| `bcrypt-password-login-demo.py` | `py -m pip install bcrypt` |
| `keystroke-logger-demo.py` | `py -m pip install pynput pygetwindow` |
| `flask-request-filter-demo.py` | `py -m pip install Flask` |
| `jwt-security-analyzer-demo.py` | `py -m pip install PyJWT` |
| `http-packet-sniffer-demo.py` | `py -m pip install scapy` |
| `flask-login-rate-limiter-demo.py` | `py -m pip install Flask Flask-Limiter` |
| `fastapi-jwt-role-access-demo.py` | `py -m pip install fastapi uvicorn PyJWT "passlib[bcrypt]" python-multipart` |

## Safety and limitations

These are learning exercises, not production security tools. Review a script before running it and use a safe lab. The web-testing scripts contain hard-coded targets; do not run them as-is or test systems without explicit authorization. Keystroke logging and packet capture can expose private information. Only use those demonstrations on your own device or network with informed consent.
