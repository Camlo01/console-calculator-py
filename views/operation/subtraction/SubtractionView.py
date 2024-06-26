from utilities.operations import Subtraction
from utilities.functionality import getValues
from views.alerts.ResultMessage import ResultMessage


def SubtractionView():
    print("")
    print("-------------------------")
    print(" - Subtraction Number - ")
    print("")
    val1, val2 = getValues()
    ResultMessage("RESULT: " + Subtraction(val1, val2))
