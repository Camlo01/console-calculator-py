from views.Home import HomeView
from views.alerts.OptionNotExist import OptionNotExist
from views.alerts.CloseMessage import CloseMessage
from views.addition.AdditionView import AdditionView
from views.subtraction.SubtractionView import SubtractionView
from views.multiplication.MultiplicationView import MultiplicationView
from views.division.DivisionView import DivisionView


# Application
def App():

    running = True
    while running:
        choice = HomeView()

        if choice == 1:
            AdditionView()
        elif choice == 2:
            SubtractionView()
        elif choice == 3:
            MultiplicationView()
        elif choice == 4:
            DivisionView()
        elif choice == 5:
            CloseMessage()
            running = False
        else:
            running = OptionNotExist()
