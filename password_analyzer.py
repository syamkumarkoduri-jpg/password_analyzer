import re
password = input("Enter Password: ")
score = 0
if len(password) >= 8:
    score += 1
else:
    print("❌ Password should be at least 8 characters")

if re.search(r"[A-Z]", password):
    score += 1
else:
    print("❌ Add an uppercase letter")

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"\d", password):
    score += 1
else:
    print("❌ Add a number")
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    print("❌ Add a special character")
if score <= 2:
    print("🔴 Weak Password")
elif score <= 4:
    print("🟡 Medium Password")
else:
    print("🟢 Strong Password")