from hexagon import Hexagon


def test1():
    hex1 = Hexagon(5, "blue")
    return hex1.area() == 64.9519052838329

def test2():
    try:
        hex2 = Hexagon(5, "красно-синий")
        hex2.draw()
        return False
    except ValueError:
        return True
    
if __name__ == '__main__':
    print("First test result:", test1())
    print("Second test result:", test2())