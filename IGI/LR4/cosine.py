import math
import statistics
from collections import Counter

class Cosine:
    def __init__(self):
        self.eps = 0.0001
        self.res = 1.0
        self.term = 1.0
        self.terms = [self.term]
        
    def calculate(self, x: float):
        """
        Calculate cosine
        
        Args:
            x (float)

        Returns:
            float: cos(x)
        """
        x = x % (2 * math.pi)
        for inum in range(1, 500):
            self.term *= (-1) * x * x / ((2 * inum - 1) * (2 * inum))
            self.res += self.term
            self.terms.append(self.res)
            if abs(self.term) < self.eps:
                break
        return self.res
    
    def get_median(self):
        """
        Calculate median
        Returns:
            float
        """
        return statistics.median(self.terms)
        
    def get_mode(self):
        """
        Calculate mode
        Returns:
            float
        """
        return statistics.mode(self.terms)
    
    def get_mean(self):
        """
        Calculate mean
        Returns:
            float
        """
        return statistics.mean(self.terms)
    
    def get_variance(self):
        """
        Calculate variance
        Returns:
            float
        """
        return statistics.variance(self.terms)
    
    def get_standart_deviation(self):
        """
        Calculate deviation
        Returns:
            float
        """
        return statistics.stdev(self.terms)