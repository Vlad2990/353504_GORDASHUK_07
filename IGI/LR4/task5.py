from matrix import Matrix, IntMatrix
from decorator import repeat_on_demand

@repeat_on_demand()
def Task5():
    """Print min element and variance of side diagonal"""
    matrix = IntMatrix(5, 5)
    matrix.fill()
    print("Matrix -\n", matrix)
    print("Min elem in side diagonal =", matrix.get_min_in_diag())
    print("Variance of side diagonal elems =", matrix.get_var_in_diag())
    print("Variance of side diagonal elems without var =", matrix.my_get_var_in_diag())
    