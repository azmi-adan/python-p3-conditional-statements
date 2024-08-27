def admin_login(username, password):
    # Check if the username is "admin" (case insensitive) and the password is "12345"
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    # Determine the message based on the temperature
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # Return "FizzBuzz" if num is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    # Return "Fizz" if num is divisible by 3 but not 5
    elif num % 3 == 0:
        return "Fizz"
    # Return "Buzz" if num is divisible by 5 but not 3
    elif num % 5 == 0:
        return "Buzz"
    # Return the number if it is not divisible by either 3 or 5
    else:
        return num

def calculator(operation, num1, num2):
    # Perform the operation based on the given operation string
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        # If the operation is invalid, print a message and return None
        print("Invalid operation!")
        return None
