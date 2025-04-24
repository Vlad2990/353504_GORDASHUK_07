import numpy as np
import statistics

class Matrix:
    def __init__(self, rows, colms):
        self.rows = rows
        self.colms = colms
        self.arr = np.empty((rows, colms))
        
    def fill(self):
        """Fill matrix with random nums"""
        self.arr =  np.random.uniform(0, 100, size=(self.rows, self.colms))
        return self
    
    def __str__(self):
        return str(self.arr)
    
class IntMatrix(Matrix):
    def __init__(self, rows, colms):
        super().__init__(rows, colms)
        
    def fill(self):
        self.arr = np.random.randint(0, 100, size=(self.rows, self.colms))
        
    def get_min_in_diag(self):
        """
        Return min value in side diag
        
        Arg: -
        
        Return: int
        """
        if self.colms != self.rows:
            return None
        return min([self.arr[i][self.rows - 1 - i] for i in range(self.rows)])
    
    def get_var_in_diag(self):
        """
        Return variance of side diag
        
        Arg: -
        
        Return: float
        """
        if self.colms != self.rows:
            return None
        return round(np.var([self.arr[i][self.rows - 1 - i] for i in range(self.rows)]), 2)
    
    def my_get_var_in_diag(self):
        """
        Return variance of side diag without using 'var'
        
        Arg: -
        
        Return: float
        """
        if self.colms != self.rows:
            return None
        diag = [self.arr[i][self.rows - 1 - i] for i in range(self.rows)]
        mean = np.mean(diag)
        variance = np.mean((diag - mean) ** 2)
        return round(variance, 2)
    
    def __str__(self):
        return super().__str__()
        