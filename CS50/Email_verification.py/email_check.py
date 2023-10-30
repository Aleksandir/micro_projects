import re

email = input("What's your email? ").strip()


def check_email(email):
    if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
        print("Valid")
        return "Valid"
    else:
        print("Invalid")
        return "Invalid"
