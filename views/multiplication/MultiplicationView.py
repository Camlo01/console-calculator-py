from utilities.operations import Multiplication
from utilities.functionality import getValues
from views.alerts.ResultMessage import ResultMessage


def MultiplicationView():
    print("")
    print("-------------------------")
    print(" - Multiplication Number - ")
    print("")
    val1, val2 = getValues()
    ResultMessage("RESULT: " + Multiplication(val1, val2))
