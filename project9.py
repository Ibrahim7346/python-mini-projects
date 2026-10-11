import random 
import time

# generate 6-digit otp
otp = random.randint(100000, 999999)

print("Your OTP is:", otp)

start_time = time.time()

user_otp = input("Enter OTP within 30 seconds: ")

if time.time() - start_time > 30:
    print("OTP Expired")

elif user_otp == str(otp):
    print("Athuntication Successful")
else:
    print("Invalid OTP")    
