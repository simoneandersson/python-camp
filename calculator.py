
def selectOperation():
    print("Select an operation:")
    print(" 1 - Add")
    print(" 2 - Subtract")
    print(" 3 - Multiply")
    print(" 4 - Divide")
    return int(input("Enter choice(1/2/3/4): "))

def calculate():
    if operation == 1:
        #Add
        return num1 + num2
    elif operation == 2:
        #Subtract
        return num1 - num2
    elif operation == 3:
        #Multiply
        return num1 * num2
    elif operation == 4:
        #Divide
        return num1 / num2
    else:
        print("You have not selected an correct operation, please try again")
        exit()

print("Welcome to Simones simple calculator!")

operation = selectOperation()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The result is: {}".format(calculate()))
exit()
