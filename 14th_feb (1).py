# Take input from user
num = int(input("Enter a number: "))

# Check positive / negative / zero
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Check even / odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Print multiplication table
print("\nMultiplication Table:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)