import json
import time
import jwt # pip install PyJWT

class JWTSecurityAnalyzer:
    def __init__(self, token: str):
        self.token = token
        self.header = {}
        self.payload = {}
        self.errors = []
        self.warnings = []
        self._parse_token()

    def _parse_token(self):
        """Splits and base64-decodes token structures safely without signature verification."""
        try:
            parts = self.token.split('.')
            if len(parts) != 3:
                raise ValueError("Invalid JWT structure. Must have 3 parts seperated by dots.")

            # decode header and payload using Pyjwt unverified tracking or manual pading fix
            self.header = jwt.get_unverified_header(self.token)
            self.payload = jwt.decode(self.token, options={"verify_signature": False})
        except Exception as e:
            self.errors.append(f"Parsing Failure: {str(e)}")

    def analyze(self):
        """Runs security heuristics across decoded metadata."""
        if self.errors:
            return {"status": "FAIL", "errors": self.errors, "warnings": []}

        self._check_algorithm()
        self._check_expiration()
        self._check_sensitive_claims()

        status = "SECURE_CANDIDATE" if not self.errors and not self.warnings else "VULNERABLE"
        return {
            "status": status,
            "header": self.header,
            "payload": self.payload,
            "errors": self.errors,
            "warnings": self.warnings
        }                
    
    def _check_algorithm(self):
       """Checks for unsafe cryptographic algorithms in the header."""
       alg = self.header.get("alg", "").upper()

       if alg == "NONE":
           self.errors.append("CRITICAL: 'alg' is set to 'none'. This allows signature bypass vulnerabilities.")
       elif alg in {"HS256", "HS384", "HS512"}:
           self.warnings.append(
               f"SYMMETRIC ALGORITHM: {alg} requires a strong, high-entropy shared secret."
           )
       elif alg not in {
           "RS256", "RS384", "RS512", "ES256", "ES384", "ES512", "EDDSA"
       }:
           self.warnings.append(f"MEDIUM-RISK: Using uncommon or legacy algorithm '{alg}'.")

    def _check_expiration(self):
        """Evaluates timestamps to enforce short-lived lifecycles."""
        now = time.time()
        exp = self.payload.get("exp")
        iat = self.payload.get("iat")

        # critical flaw missing expiration
        if not exp:
            self.errors.append("HIGH-RISK: 'exp' (Expiration Time) claim is missing. Token never expires.")
        else:
            if exp < now:
                self.warnings.append("INFO: Token is already expired.")
            elif (exp - (iat or now)) > 86400: # over 24 hours
                self.warnings.append("MEDIUM-RISK: Token lifespan is unusually long (geater than 24 hours).")

    def _check_sensitive_claims(self):
        """Detects presence of structural identity tracking validation fields."""
        if not self.payload.get("iss"):
            self.warnings.append("LOW-RISK: 'iss' (Issuer) claim is missing. Harder to validate context origination.")
        if not self.payload.get("aud"):
            self.warnings.append("LOW-RISK: 'aud' (Audience) claim is missing. Vulnerable to target reuse.")

# example usage
if __name__ == "__main__":
    # vulnerable example token (signed with alg: none)
    bad_token ="eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ."
    
    analyzer = JWTSecurityAnalyzer(bad_token)
    results = analyzer.analyze()
    print(json.dumps(results, indent=2))
       
