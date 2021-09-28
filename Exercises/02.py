# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5

def cascade(num):
    for num in range(num+1):
        for i in range(num):
            print (num, end=" ")
        print("\n")

num = int(input("Enter a Num: "))
cascade(num)
