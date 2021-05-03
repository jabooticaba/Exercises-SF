class Rectangle:
    def __init__(self, wight, height):
        self.wight = wight
        self.height = height
        
    def getWight(self):
        return self.wight
    
    def getHeight(self):
        return self.height
    
    def getArea(self):
        return self.wight * self.height
