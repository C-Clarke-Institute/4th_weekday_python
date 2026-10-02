

def multiply(a, b):
    return a * b

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return 'Cannot be divided by zero'

    return a / b

def take_user_inputs():
    first_num = int(input("Enter first number - : "))
    second_num = int(input("Enter second number - : "))
    return first_num,second_num


while True:
    operation = input("Enter Operation to continue (+,-,/,*) : ")
    if operation == "+":
        val1, val2 = take_user_inputs()
        print(f"Result is {addition(val1, val2)}")
    elif operation == "-":
        val1, val2 = take_user_inputs()
        print(f"Result is {substraction(val1, val2)}")
    elif operation == "/":
        val1, val2 = take_user_inputs()
        print(f"Result is {division(val1, val2)}")

