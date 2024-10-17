def addition(num1,num2):
    return num1 + num2
    
def subtraction(num1,num2):
    return num1 - num2
    
def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number"))

print("Choose an operation")


operation = str(input('+ , - , * , / '))

if operation == "+":
    result = addition(num1, num2)
    print(f"{result} ")
elif operation == "-":
    result = substraction(num1, num2)
    print(f"{result} ")
elif operation == "*":
    result = multiplication(num1, num2)
    print(f"{result} ")
elif operation == "/":
    result = division(num1, num2)
    print(f"{result} ")
else:
    print("error")