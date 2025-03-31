import math
from input_check import input_float
from decorator import repeat_on_demand

"""
Lab Work #1
Gordashuk Vladislav
This module calcule cosine with Taylor series
Version: 1.0
Date: 30.03.2025
"""

def F(x):
    """
    The function counts the Taylor series expansion for the cosine

    Arg: float num

    Return: cos(num)
    """
    x = x % (2 * math.pi)
    eps=0.0001
    res = 1.0
    term = 1.0
    inum = 0
    fres = math.cos(x)
    for inum in range(1, 500):
        term *= (-1) * x * x / ((2 * inum - 1) * (2 * inum))
        res += term
        if abs(term) < eps:
            break
    return res, inum

def Output(x, n, res, fres, eps):
    """Display result"""
    print("| {:^5} | {:^5} | {:^10} | {:^10} | {:^5} |".format("x", "n", "F(x)", "Math F(x)", "eps"))
    print("-" * 50)
    print("| {:^5.2f} | {:^5} | {:^10.6f} | {:^10.6f} | {:^5.5f} |".format(x, n, res, fres, eps))

@repeat_on_demand()
def Task1():
    print("\n" + "="*40)
    print("Calculate cos")
    num = input_float()
    n = 0
    res, n = F(num)
    Output(num, n, res, math.cos(num), 0.0001)
