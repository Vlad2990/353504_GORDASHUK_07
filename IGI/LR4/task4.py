from hexagon import Hexagon
from input_check import input_int
from decorator import repeat_on_demand

@repeat_on_demand()
def Task4():
    """Draw hexagon with entered parameters"""
    a = input_int()
    while True:
        try:
            color = input("Input color: ")
            title = input("Input title: ")
            hex = Hexagon(a, color)
            hex.draw(title=title)
        except ValueError:
            print("Wrong color")
        else:
            print(hex)
            break
