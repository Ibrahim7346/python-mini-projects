import re
import hashlib
import bcrypt
import requests

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 character long")

    # 2. Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # 3. Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # 4. Numbers
    if re.search(r"[0-9]", password):
        score += 1

    else:   
        feedback.append("Add at least one number")

    # 5. Special Characters
    if re.search("[!@#$%^&*(_+:,.<>]", password):
        score += 1

    else:
        feedback.append("Add at least one special character")

    print("\nScore:", score, "/5")
    for f in feedback:
         print("-", f)
         
    # Final evaluation
    if score == 5:
            strength = "Very Strong"
    elif score >= 3:
            strength = "Moderate"
    else:
            strength = "Weak"

    return strength, feedback

password =  input("Enter your password: ")
strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if feedback:
    print("\nsuggestion:")
    for item in feedback:
        print("-", item)
            