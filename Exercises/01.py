#Given two integer numbers return their product only if the product is greater than 1000, else return their sum.

num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))

if (num1 * num2) > 1000:
    print(num1 * num2)
else:
    print(num1 + num2)
