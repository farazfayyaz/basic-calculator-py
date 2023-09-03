# addition function
def add (num1, num2):
    answer = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(answer))

# subtraction function
def sub (num1, num2):
    answer = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(answer))

# multiplication function
def mult (num1, num2):
    answer = num1 * num2
    print(str(num1) + " * " + str(num2) + " = " + str(answer))

# division function
def div (num1, num2):
    answer = num1 / num2
    print(str(num1) + " / " + str(num2) + " = " + str(answer))

# while loop to keep repeating the choices until user chooses exit
while True:
    # choices to activate functions
    print("A - Addition")
    print("B - Subtraction")
    print("C - Multiplication")
    print("D - Division")
    print("E - Exit")


    # input for user's choice: add, sub, mult or div
    choice = input("Enter your choice: ")


    # checks choice then runs function and prints results
    if choice == "A" or choice == 'a':
        print('Addition')
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        add(num1, num2)
    elif choice == "B" or choice == "b":
        print('Subtraction')
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        sub(num1, num2)
    elif choice == "C" or choice == "c":
        print('Multiplication')
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        mult(num1, num2)
    elif choice == "D" or choice == "d":
        print('Division')
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        div(num1, num2)
    elif choice == "E" or choice == "e":
        print("Program Ended")
        quit()