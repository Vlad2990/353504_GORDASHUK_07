"""
Lab Work #1
Gordashuk Vladislav
This module implements the functions of checking the input
and initialization of the list
Version: 1.0
Date: 30.03.2025
"""

def input_int():
    """
    Continuously prompts the user to input an integer until a valid one is entered.

    Arg: -
    
    Returns: int
        
    """
    while True:
        try:
            num = int(input("Input integer: "))
            return num
        except ValueError:
            print("Wrong num. Retry")


def input_float():
    """
    Continuously prompts the user to input a float until a valid one is entered.

    Arg: -
    
    Returns: float 
    """
    while True:
        try:
            num = float(input("Input float: "))
            return num
        except ValueError:
            print("Wrong num. Retry")


def input_int_with_num(num):
    """
    Attempts to convert a string to an integer.
    
    Arg: num - The string to convert to integer.
        
    Returns: int | None
    """
    try:
        return int(num)
    except ValueError:
        print("Wrong num. Retry")
        return None


def inp_seq(n: int):
    """
    Collects a sequence of n integers from user input.
    
    Arg: n - The number of integers to collect.
        
    Returns: list[int]
    """
    arr = []
    print("Input list")
    for i in range(n):
        num = input_int()
        arr.append(num)
    return arr


def input_float_with_num(num):
    """
    Attempts to convert a string to a float.
    
    Arg: num - The string to convert to float.
        
    Returns: float | None
    """
    try:
        return float(num)
    except ValueError:
        print("Wrong num. Retry")
        return None


def inp_seq_float(n):
    """
    Collects a sequence of n floating-point numbers from user input
    
    Arg: n - The number of floats to collect
        
    Returns: list[float]
    """
    arr = []
    print("Input list")
    for i in range(n):
        num = input_float()
        arr.append(num)
    return arr


def seq_generate(n):
    """
    Generates a sequence of integers from 1 to n (inclusive)
    
    Arg: n - The upper bound of the sequence
        
    Returns: list[int]
    """
    for i in range(1, n + 1):
        yield i
