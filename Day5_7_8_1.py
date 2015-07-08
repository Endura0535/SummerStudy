import math

class Shape:
    perimeter = 0
    area = 0

    def calcArea(self):
         pass
    def calcPerimeter(self):
        pass
    def printInfo(self):
        print "Area : {0}, Perimeter : {1}".format(self.area, self.perimeter)

class Rectangle(Shape):
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calcArea(self):
        self.area = self.x*self.y
    def calcPerimeter(self):
        self.perimeter = 2*(self.x+self.y)

rect = Rectangle(2, 4)
rect.calcArea()
rect.calcPerimeter()
rect.printInfo()

class Triangle(Shape):
    length = 0

    def __init__(self,length):
        self.length = length
    def calcArea(self):
        self.area = math.sqrt(3)/4*self.length*self.length
    def calcPerimeter(self):
        self.perimeter = 3*self.length

tri = Triangle(3)
tri.calcArea()
tri.calcPerimeter()
tri.printInfo()

class Circle(Shape):
    r = 0

    def __init__(self,r):
        self.r = r
    def calcArea(self):
        self.area = self.r*self.r*3.14
    def calcPerimeter(self):
        self.perimeter = 2*3.14*self.r

cir = Circle(4)
cir.calcArea()
cir.calcPerimeter()
cir.printInfo()