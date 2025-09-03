first_number = int(input("please your first number: "))

second_number = int(input("please your second number: "))

# Addition operation
print(first_number + second_number)

# Subtraction operation
print(first_number - second_number)

# Multiplication operation
print(first_number * second_number)

# Division operation with error handling
try:
    print(first_number / second_number)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")