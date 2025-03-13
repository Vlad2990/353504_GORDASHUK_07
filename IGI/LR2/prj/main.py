import square
import circle

R = int(input("Input radius of circle: "))
print("Perimetr - ", circle.perimeter(R))
print("Area - ", circle.area(R))

a = int(input("Input side length of square: "))
print("Perimetr - ", square.perimeter(a))
print("Area - ", square.area(a))