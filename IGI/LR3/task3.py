from decorator import repeat_on_demand

"""
Lab Work #1
Gordashuk Vladislav
This module counts the number of nums and chars in string
Version: 1.0
Date: 30.03.2025
"""

def CheckString():
    """
    Counts the number of lowercase letters
    and the number of digits

    Arg: -

    Return: Num of letters and num of numbers
    """
    numCount = 0
    charCount = 0
    for char in input():
        if char.isdigit():
            numCount += 1
        elif char.islower():
            charCount += 1
    return charCount, numCount


@repeat_on_demand()
def Task3():
    print("\n" + "="*40)
    print("Input string: ")
    chars, nums = CheckString()
    print("String has", chars, "lowercase char and", nums, "numbers")
