from input_check import input_int
from decorator import repeat_on_demand

"""
Lab Work #1
Gordashuk Vladislav
This module counts the number of nums < 10 in input cycle
Version: 1.0
Date: 30.03.2025
"""

def InputCycle():
    """
    Loop that takes integers
    and counts the number of numbers less than 10
    
    Arg: -

    Return: Num of numbers
    """
    count = 0
    num = input_int()
    while num != 100:
        if num < 10:
            count += 1
        num = input_int()
    return count

@repeat_on_demand()
def Task2():
    print("\n" + "="*40)
    print("Input sequence. Type '100' to stop")
    num = InputCycle()
    print("Num of numbers less than 10 -", num)
