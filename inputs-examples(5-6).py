# getting input - getting variable values from the user via the keyboard
    # the built in function for this is called 'input'
        # the syntax is input([prompt])

prompt = 'What is the speed of the car?'
speed = input (prompt)
print("The speed of the car is:", speed)

# catching and handling exceptions
# we can use the 'try' and 'except' statements that will not crash the code in case of an exception

try:
    num = input("Give me a number")
    num = int(num)
    print("The square of the number read is:", num*num)
except:
    print("Please give me a proper number")

# If no exceptions happen in the 'try' block, then the execution ignores the 'except' blocks
# If an exception happen, the execution in the try block stops and the except block that matches
    # the name of the exception is executed

try:
    num = input("Give me a number")
    num = int(num)
    num2 = input("Give me another number")
    num2 = int(num2)
    result = num / num2
    print("The division result is", result)
except ValueError:
    print("Please give me a proper number")
except ZeroDivisionError:
    print("The second number cannot be zero")

