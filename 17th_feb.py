def fizzbuzz():
    # Take input for the range
    try:
        limit = int(input("Enter the limit (e.g., 50): "))
    except ValueError:
        print("Invalid input. Using default limit of 50.")
        limit = 50

    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    print(f"\n--- FizzBuzz Results (1 to {limit}) ---")
    
    for i in range(1, limit + 1):
        # Check for both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(i)

    # Display the counts as required by the assignment
    print("\n--- Count Summary ---")
    print("Fizz count (Divisible by 3):", fizz_count)
    print("Buzz count (Divisible by 5):", buzz_count)
    print("FizzBuzz count (Divisible by both):", fizzbuzz_count)

# Call the function
fizzbuzz()