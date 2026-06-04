import random

print("===== OTP Verification System =====")

# Generate 6-digit OTP
otp = random.randint(100000, 999999)

# Display OTP (for learning purposes)
print("Your OTP is:", otp)

# User enters OTP
user_otp = int(input("Enter the OTP: "))

if user_otp == otp:
    print("OTP Verified Successfully!")
else:
    print("Invalid OTP!")