import math
# Basic Calculations
def basic_calc():
    print("Basic Arithmetic of only two numbers.")
    number1 = float(input("Enter The First Number: "))
    op = input("Enter the operator (+,-,/,*): ")
    number2 = float(input("Enter The Second Number: "))

    if op == '+':
        print(number1 + number2)
    elif op == '/':
        print(number1 / number2)
    elif op == '-':
        print(number1 - number2)
    elif op == '*':
        print(number1 * number2)
    else:
        print("Syntax Error :(")
def trig_func():
    number1 = float(input("Enter an Angle: "))
    print("Select the Trigonometric Function:\n1. Sin\n2. Arc Sin\n3. Cos\n4. Arc Cos\n5. Tan\n6. Arc Tan")
    trig_choice = input("Choose: ")
    if trig_choice == '1':
        print(f'sin({number1}) = ',math.sin(number1))
    elif trig_choice == '2':
        print(f'arc sin({number1}) = ',math.asin(number1))
    elif trig_choice == '3':
        print(f'cos({number1}) = ',math.cos(number1))
    elif trig_choice == '4':
        print(f'arc cos({number1}) = ',math.acos(number1))
    elif trig_choice == '5':
        print(f'tan({number1}) = ',math.tan(number1))
    elif trig_choice == '6':
        print(f'arc tan({number1}) = ',math.atan(number1))
    else:
        print("Invalid Choice :(")
# Square Root
def square_root_func():
    number = float(input("Enter a number: "))
    print(math.sqrt(number))

# Square
def squares():
    number = float(input("Enter a number: "))
    print(f"{number} squared is ",number**2)

# Cube
def cube():
    number = float(input("Enter a number: "))
    print(f"{number} cubed is ",number**3)

# Log
def log_func():
    number = float(input("Enter a number: "))
    print(math.log10(number))

print("INTEGRATED CALCULATOR.")
while True:
    print("Choose an option:")
    print("1. Basic Arithmetic Operations.\n2. Trigonometric Functions.\n3. Square Root.\n4. Square a number.\n5. Cube a number.\n6. Log base 10.\n7. Exponential.")
    choice = input("Enter your choice: ")

    if choice == '1':
        basic_calc()
        break

    elif choice == '2':
        trig_func()
        break

    elif choice == '3':
        square_root_func()
        break

    elif choice == '4':
        squares()
        break

    elif choice == '5':
        cube()
        break

    elif choice == '6':
        log_func()
        break
    else:
        print("Choice not available...................")
def basic_calc()
