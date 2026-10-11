# Python Mini Projects

Small Python and cybersecurity learning projects. Each script is linked below with a short description of what it demonstrates.

## Projects

| Script | What it does / learning use |
|---|---|
| [dns-lookup-tool.py](dns-lookup-tool.py) | Looks up a domain's IP address and hostname using Python's DNS/socket tools. |
| [common-tcp-port-scanner.py](common-tcp-port-scanner.py) | Checks a short list of TCP ports on a host you own or are authorized to assess. |
| [password-strength-checker.py](password-strength-checker.py) | Scores a typed password against basic length and character rules and suggests improvements. |
| [caesar-cipher-encryptor.py](caesar-cipher-encryptor.py) | Demonstrates how a simple Caesar letter-shift cipher works; it is for learning, not secure encryption. |
| [suspicious-url-checker.py](suspicious-url-checker.py) | Flags a few URL patterns for review; it is a basic exercise, not a reliable phishing detector. |
| [bcrypt-password-login-demo.py](bcrypt-password-login-demo.py) | Demonstrates hashing a password with bcrypt and checking a login attempt. |
| [ip-geolocation-lookup.py](ip-geolocation-lookup.py) | Requests approximate geolocation and ISP details for an IP address from an external service. |
| [sha256-file-hash-checker.py](sha256-file-hash-checker.py) | Calculates a file's SHA-256 checksum so you can compare file integrity. |
| [firewall-rule-simulator.py](firewall-rule-simulator.py) | Simulates adding and checking blocked IP addresses in memory; it does not change system firewall rules. |
| [three-letter-password-guessing-demo.py](three-letter-password-guessing-demo.py) | Demonstrates a tiny, hard-coded three-letter guessing loop; use only as a local educational example. |
| [timed-otp-demo.py](timed-otp-demo.py) | Demonstrates a six-digit code with a time limit; the code is shown in the same terminal, so this is not real authentication. |
| [keystroke-logger-demo.py](keystroke-logger-demo.py) | Demonstrates keyboard event logging and active-window labels. It records sensitive input: only run on your own device with informed consent. |
| [reflected-xss-form-checker-lab.py](reflected-xss-form-checker-lab.py) | Demonstrates basic reflected-XSS checks against web forms. The current example target is hard-coded; do not run it against a site without explicit authorization. |
| [sql-error-signature-checker-lab.py](sql-error-signature-checker-lab.py) | Demonstrates checking a response for database error text. Its example target is hard-coded; do not run it against a site without explicit authorization. |
| [flask-request-filter-demo.py](flask-request-filter-demo.py) | Runs a small local Flask app that rejects requests matching a few illustrative WAF patterns. |
| [jwt-security-analyzer-demo.py](jwt-security-analyzer-demo.py) | Decodes JWT metadata without verifying the signature and flags selected claims and algorithms; it does not prove a token is secure. |
| [http-packet-sniffer-demo.py](http-packet-sniffer-demo.py) | Demonstrates viewing TCP traffic on port 80 with Scapy. Packet contents can be sensitive; capture only on a network you own or are authorized to monitor. |
| [md5-file-signature-scanner-demo.py](md5-file-signature-scanner-demo.py) | Demonstrates matching file MD5 hashes against a tiny sample list; this is not a production malware scanner. |
| [flask-login-rate-limiter-demo.py](flask-login-rate-limiter-demo.py) | Demonstrates a Flask login endpoint with basic IP rate limits and in-memory account lockouts. |
| [fastapi-jwt-role-access-demo.py](fastapi-jwt-role-access-demo.py) | Demonstrates a FastAPI login flow with JWTs and role-checked routes using mock users. |
| [wordlist-hash-checker-demo.py](wordlist-hash-checker-demo.py) | Demonstrates checking a supplied wordlist against a hash you are authorized to audit. |

## How to run

Install Python 3, download or clone this repository, then run a script from its folder:

```bash
python dns-lookup-tool.py
```

Replace the filename with the script you want to try. Some scripts need third-party packages; install only the dependencies used by that script (for example, `requests`, `beautifulsoup4`, `bcrypt`, `flask`, `flask-limiter`, `PyJWT`, `scapy`, `fastapi`, `passlib[bcrypt]`, or `uvicorn`). Network, packet-capture, and security-testing scripts need extra setup and authorization.

These are learning exercises, not production security tools. Review a script before running it, use a safe lab, and only test systems and networks you own or have permission to assess.
