# Develop a simple calculator

def calculator(num1, operator, num2):
    if (operator == "+"):
        result = num1 + num2
        print("Result = ", result)
    elif (operator == "-"):
        result = num1 - num2
        print("Result = ", result)
    elif (operator == "*"):
        result = num1 * num2
        print("Result = ", result)
    elif (operator == "/"):
        result = num1 / num2
        print("Result = ", result)
    else:
        print("The Operator Entered is not Valid!")

num1 = float(input("Enter First Num: "))
operator = (input("Enter the Operator: "))
num2 = float(input("Enter Second Num: "))

calculator(num1, operator, num2)
