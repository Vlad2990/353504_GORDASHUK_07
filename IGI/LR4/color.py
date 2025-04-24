class Color():
    def __init__(self, color: str):
        self._color = color
    
    def color(self, value):
        self._color = value
        
    def setcolor(self, value):
        self._color = value
        
    def getcolor(self):
        return self._color
    
    color = property(getcolor, setcolor)