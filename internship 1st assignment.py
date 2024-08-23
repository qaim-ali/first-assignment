def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def subtraction(a, b):
    return a - b

def modulus(a, b):
    return a % b

def division(a, b):
    return a / b

print("\n\t\t\t\tSIMPLE CALCULATOR\n")
print("\tPlease Select The Operation Which You Want To Perform:\n")
print("\t\tADDITION (enter add)")
print("\t\tSUBTRACTION (enter sub)")
print("\t\tMULTIPLICATION (enter mul)")
print("\t\tDIVISION (enter div)")
print("\t\tMODULUS (enter mu)")
print("\t\tQUIT (enter q)\n")

while True:
    enter = input("Enter The Operation: ").strip().lower()
    
    if enter == "q":
        print("Exiting the calculator. Goodbye!")
        break
    elif enter in ["add", "sub", "mul", "div", "mu"]:
        a = eval(input("Enter first number: "))
        b = eval(input("Enter second number: "))
        
        if enter == "add":
            print("Your answer is =", addition(a, b))
        elif enter == "sub":
            print("Your answer is =", subtraction(a, b))
        elif enter == "mul":
            print("Your answer is =", multiplication(a, b))
        elif enter == "div":
            print("Your answer is =", division(a, b))
        elif enter == "mu":
            print("Your answer is =", modulus(a, b))
    else:
        print("Invalid Operation Selected. Please try again.")
