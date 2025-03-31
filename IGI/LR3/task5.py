from input_check import inp_seq_float, input_int, seq_generate
from decorator import repeat_on_demand

"""
Lab Work #1
Gordashuk Vladislav
This module requests a list from the user and finds
in it the number of numbers greater than the entered one,
and also the product of the numbers after the maximum value.
Version: 1.0
Date: 30.03.2025
"""

def FindHigher(arr, c):
    """
    Сounts the number of numbers greater than the specified one

    Arg: list, int num

    Return: Count of num
    """
    count = 0
    for num in arr:
        if num > c > 0:
            count += 1
    return count

def FindMul(arr):
    """
    Find the product of the array elements
    located after the element with the largest value

    Arg: list

    Return: Product of num
    """
    maxNum = max(arr)
    if arr.index(maxNum) == len(arr) - 1:
        print("There are no elements after max elem")
        return 0
    res = 1.0
    for num in arr[arr.index(maxNum)+1:]:
        res *= num
    return res

def PrintOptions():
    print("\n1 - Get num of nums < 0 and < C")
    print("2 - Get multiplying numbers after the maximum number")
    print("3 - Get list")
    print("4 - End")

@repeat_on_demand()
def Task5():
    print("\n" + "="*40)
    print("Input C")
    c = input_int()
    print("\nInput list size")
    n = input_int()
    while n <= 0:
        print("Input n > 0")
        n = input_int()
              
    print("\n1 - Generate list")
    print("2 - Initialize manually")
    while True:
        flag = input()
        if flag == '1':
            arr = seq_generate(n)
            break
        elif flag == '2':
            arr = inp_seq_float(n)
            break
        else:
            print("Wrong num")
    PrintOptions()
    while True:
        flag = input()
        if flag == '1':
            print("\nNum of nums greater than C -", FindHigher(arr, c))
            PrintOptions()
        elif flag == '2':
            print("\nMultiplying numbers after the maximum number -", FindMul(arr))
            PrintOptions()
        elif flag == '3':
            print("\nList:", arr)
            PrintOptions()
        elif flag == '4':
            return
        else:
            print("Wrong num")
