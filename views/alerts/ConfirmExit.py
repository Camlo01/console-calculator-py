def ConfirmExit():
    print("-------------------------")
    print("- Estás seguro que quieres")
    print("- cerrar la calculadora ?")
    print(" Continuar -> 1")
    print(" Cerrar  -> 0")
    print("")
    print("")
    optionSelected = int(input("Opcion: "))
    
    if optionSelected == 1:
        return True
    else:
        return False
    
    