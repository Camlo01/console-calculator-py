from utilities.operations import Addition
from utilities.functionality import getValues
from views.alerts.ResultMessage import ResultMessage


def AdditionView():
    print("")
    print("-------------------------")
    print(" - Addition Number - ")
    print("")
    val1, val2 = getValues()
    ResultMessage("RESULT: " + Addition(val1, val2))
