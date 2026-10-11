import bcrypt

# register
username = input("Create username: ")
password = input("Create password: ")

# convert password to bytes
password_bytes = password.encode('utf-8')

# hash password
hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print("\nRegistration Successful!")
print("Stored Hash:", hashed_password)

# login
print("\n--- Login ---")

login_password = input("Enter password: ")

if bcrypt.checkpw(login_password.encode('utf-8'), hashed_password):
    print("Login Successful")
else:
    print("Incorrect Password")    