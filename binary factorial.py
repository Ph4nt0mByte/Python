n = int(input("Enter a number: "))
binary = ""

while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2

print("Binary representation:", binary)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is", result)