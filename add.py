while True:
    print("This program will add 2 integers together")
    try:
        num1 = int(input("Enter first number: "))
    except ValueError:
        print("You have to enter an integer!")
        break
    try:
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("You have to enter an integer!")
        break
    print(f"The sum of these two numbers is {num1 + num2}")