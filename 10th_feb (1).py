# 1. Check odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# 2. Print numbers from 10 to 1
print("\nNumbers from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

# 3. Sum until user enters 0
total = 0
while True:
    n = int(input("\nEnter a number (0 to stop): "))
    if n == 0:
        break
    total += n
print("Total sum:", total)