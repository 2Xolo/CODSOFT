while True:
    print("-----------------------------------------------------------------")
    print("1. Subtraction") 
    print("2. Add")
    print("3. Multiplication.")
    print("4. Division")
    print("-----------------------------------------------------------------")
    print("Press X or exit to exit")

    choice = input("Enter your choice : ")

    if choice.lower() == 'x' or choice.lower() == 'exit':
        break

    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))


    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    print("-----------------------------------------------------------------")
    print("The Total is : ")
    if choice == "1":
        print(num1, "-", num2, "=", sub)

    elif choice == "2":
        print(num1, "+", num2, "=", add)

    elif choice == "3":
        print(num1, "*", num2, "=", mult)

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            div = num1 / num2
            print(num1, "/", num2, "=", div)

    else:
        print("Invalid choice")
