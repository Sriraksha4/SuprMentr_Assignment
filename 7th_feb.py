import re

def check_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    elif not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    elif not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."
    elif not re.search("[0-9]", password):
        return "Password must contain at least one digit."
    elif not re.search("[@#$%^&+=!]", password):
        return "Password must contain at least one special character."
    else:
        return "Strong Password ✅"

password_input = input("Enter your password: ")
print(check_password(password_input))