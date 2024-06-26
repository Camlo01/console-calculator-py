from utilities.operations import Division
from utilities.functionality import getValues
from views.alerts.ResultMessage import ResultMessage


def DivisionView():
    print("")
    print("-------------------------")
    print(" - Division Number - ")
    print("")
    val1, val2 = getValues()
    ResultMessage("RESULT: " + Division(val1, val2))
