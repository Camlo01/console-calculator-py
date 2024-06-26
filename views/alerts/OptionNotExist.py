def OptionNotExist():
    print("")
    print("-------------------------")
    print("- This option does not")
    print("exist !!!")
    print("")
    print("- Close calculator?")
    print(" Continue  -> 1")
    print(" Close     -> 0")
    print("")
    optionSelected = int(input("Option: "))

    if optionSelected == 1:
        return True
    else:
        return False
    
    return False
