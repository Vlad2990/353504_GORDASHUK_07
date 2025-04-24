from shape import Shape
from color import Color
import math
import matplotlib.pyplot as plt


class Hexagon(Shape):
    shape_type = "Hexagon"
    def __init__(self, a: float, color: str):
        self.a = a
        self.color = Color(color)

        self.x_points = [a, 
                    a / 2, 
                    -a / 2,
                    -a, 
                    -a / 2, 
                    a / 2,
                    a]

        self.y_points = [0,
                    a * math.sqrt(3) / 2,
                    a * math.sqrt(3) / 2,
                    0,
                    -a * math.sqrt(3) / 2,
                    -a * math.sqrt(3) / 2,
                    0]
        
    def draw(self, color="", title=""):
        """
        Draw hexagon with params

        Args:
            color (str, optional): _description_. Defaults to "".
            title (str, optional): _description_. Defaults to "".
        """
        if color:
            self.color.color(color)
        if title:
            plt.title(title)
        plt.fill(self.x_points, self.y_points, color=self.color.color)
        plt.show()
        plt.savefig("shape.png")
        
    def area(self) -> float:
        return self.a * self.a * 3 * math.sqrt(3) / 2
    
    def __str__(self):
        return "Shape: {}, Color: {}, a: {}".format(
            self.shape_type,
            self.color.color,
            self.a
)