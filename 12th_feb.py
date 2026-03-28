name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

if age < 18:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

print(f"Hello {name}! You are an {category} and you enjoy {hobby}.")