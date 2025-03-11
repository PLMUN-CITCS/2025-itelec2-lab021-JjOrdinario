# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Input from user
num = int(input("Enter a non-negative integer: "))

# Check if the number is valid
if num < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"The factorial of {num} is: {factorial(num)}")
