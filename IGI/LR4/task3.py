import math
import numpy as np
import matplotlib.pyplot as plt
from cosine import Cosine
from input_check import input_float
from decorator import repeat_on_demand

def Output(x, n, res, fres, eps):
    """Display result"""
    print("| {:^5} | {:^5} | {:^10} | {:^10} | {:^5} |".format("x", "n", "F(x)", "Math F(x)", "eps"))
    print("-" * 50)
    print("| {:^5.2f} | {:^5} | {:^10.6f} | {:^10.6f} | {:^5.5f} |".format(x, n, res, fres, eps))

@repeat_on_demand()
def Task3():
    """Calculate cosine and plotting"""
    cos = Cosine()
    x = input_float()
    res = cos.calculate(x)
    
    x_vals = np.linspace(0, 2 * math.pi, len(cos.terms))
    y_vals = cos.terms
    
    print("Cos =", res)
    print("Mode =", cos.get_mode())
    print("Mean =", cos.get_mean())
    print("Median =", cos.get_median())
    print("Variance =", cos.get_variance())
    print("Standart deviation =", cos.get_standart_deviation())
    
    Output(x, len(cos.terms), res, math.cos(x), cos.eps)
    
    plt.plot(x_vals, y_vals, color="blue", label="my cos")
    plt.axhline(y=math.cos(x), color="red", linestyle="--", label="math.cos")
    plt.xlabel('n')
    plt.ylabel('F(x)')
    plt.legend()
    plt.grid(True)
    plt.title("Math.cos and Taylor series expansion compare")

    plt.savefig("task3.png")

    plt.show()