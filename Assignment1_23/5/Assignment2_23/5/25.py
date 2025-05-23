#Write a program to handle errors, the program should ask for two numbers using the input() and then divide them.
#Use an infinite loop to keep asking until the input is provided.
import math

x = int(input("Enter number1"))
y = int(input("Enter number2"))
print(x)
print(y)
while x > y or x < y:
    try:
            result = x / y
    except:
        print("This code has an error")
    else:
             print("The answer is:", result)
    finally:
        print("The execution is done")
        break