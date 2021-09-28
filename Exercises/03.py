# Print multiplication table form x to y

def multiplication_table(x, y):
    for i in range(x, y):
        for j in range(x, y):
            print(i * j, end=" ")
        print("\t\t")

x = int(input("Enter First Num: "))
y = int(input("Enter Second Num: "))
multiplication_table(x, y)
