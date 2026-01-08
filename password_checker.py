
import re

password = input("Enter a password to test: ")

length_check = len(password) >= 8
digit_check = re.search(r"\d", password)
upper_check = re.search(r"[A-Z]", password)
lower_check = re.search(r"[a-z]", password)
special_check = re.search(r"[!@#$%^&*()_+=\-]", password)

if all([length_check, digit_check, upper_check, lower_check, special_check]):
    print("✅ Strong password")
else:
    print("❌ Weak password")
    print("Tips:")
    if not length_check:
        print("- Use at least 8 characters")
    if not digit_check:
        print("- Add numbers")
    if not upper_check:
        print("- Add uppercase letters")
    if not lower_check:
        print("- Add lowercase letters")
    if not special_check:
        print("- Add special characters")
