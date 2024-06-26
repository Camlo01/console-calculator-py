def HomeView():
    print("-------------------------")
    print("- WELCOME TO CALCULATOR -")
    print("-------------------------")
    print("")
    print("Select operation!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("")

    valueEntered = 0
    try:
        valueEntered = int(input("Choose an option: "))
    except ValueError:
        print("-------------------------")
        print("---------ERROR-----------")
        print("-------------------------")
        print("")
        print("- Please enter a number")

    return valueEntered
