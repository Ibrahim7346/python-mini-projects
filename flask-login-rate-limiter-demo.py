import time
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# initialise rate limiter using client ip addresses
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://" # use redis ('redis://localhost:6379') in production
)
# in-memory tracking for failed attempts per username (for account lockout)
# in production, use a database or a shared redis cache instead.
FAILED_ATTEMPTS = {}
LOCKOUT_DURATION = 300 # 5 minutes in seconds
MAX_FAILED_ATTEMPTS = 5

def is_account_locked(username):
    """Check if a specific user account is temporarily locked."""
    if username in FAILED_ATTEMPTS:
        attempts, lock_time = FAILED_ATTEMPTS[username]
        if attempts >= MAX_FAILED_ATTEMPTS:
            if time.time() - lock_time < LOCKOUT_DURATION:
                return True
            else:
                # lockout expired; reset tracking
                del FAILED_ATTEMPTS[username]
    return False

def record_failed_attempt(username):
    """Increments the failed attempt counter for a user account."""
    if username not in FAILED_ATTEMPTS:
        FAILED_ATTEMPTS[username] = [1, 0]
    else:
        FAILED_ATTEMPTS[username] [0] += 1

    if FAILED_ATTEMPTS[username] [0] >= MAX_FAILED_ATTEMPTS:
        FAILED_ATTEMPTS[username] [1] = time.time() # set lockout timestamp

def reset_failed_attempts(username):
    """Clears failed attempts upon a successful login."""
    if username in FAILED_ATTEMPTS:
        del FAILED_ATTEMPTS[username]

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute", error_message="Too many login attemptfrom this IP. Try again later.")
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400

    # check if the user account is locked out globally
    if is_account_locked(username):
        return jsonify({"error": "Account temporarily locked due to too many failures. try again later."}), 423

    # mock authentication evaluation (replace with actual database verification)
    is_valid_user = (username == "admin" and password == "SecurePass123!")

    if is_valid_user:
        reset_failed_attempts(username)
        return jsonify({"message": "Login successful!"}), 200
    else:
        record_failed_attempt(username)
        # use a generic error message to prevent username enumeration
        return jsonify({"error": "Invalid username or password"}), 401
    
@app.errorhandler(429)
def ratelimit_handler(e):
    """Custom response structure for IP rate limits."""
    return jsonify({"error": f"IP Rate limit exceeded: {e.description}"}), 429

if __name__ == '__main__':
    app.run(debug=True)    




