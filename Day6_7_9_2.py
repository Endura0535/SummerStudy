import math

class Shape:
    area = 0
    def calcArea(self):
        pass

class TwoDim(Shape):
    perimeter = 0
    def calcPerimeter(self):
        pass

class Rectangle(TwoDim):
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calcArea(self):
        self.area = self.x*self.y
    def calcPerimeter(self):
        self.perimeter = 2*(self.x+self.y)
    def printInfo(self):
        print "Area : {0}, Perimeter : {1}".format(self.area, self.perimeter)

class Triangle(TwoDim):
    a = 0
    def __init__(self,a):
        self.a = a
    def calcArea(self):
        self.area = math.sqrt(3)/4*self.a*self.a
    def calcPerimeter(self):
        self.perimeter = 3*self.a
    def printInfo(self):
        print "Area : {0}, Perimeter : {1}".format(self.area, self.perimeter)

class Circle(TwoDim):
    r = 0
    def __init__(self,r):
        self.r = r
    def calcArea(self):
        self.area = self.r*self.r*3.14
    def calcPerimeter(self):
        self.perimeter = 2*3.14*self.r
    def printInfo(self):
        print "Area : {0}, Perimeter : {1}".format(self.area, self.perimeter)

class ThreeDim(Shape):
    volume = 0
    def calcVolume(self):
        pass

class Cube(ThreeDim):
    a = 0
    def __init__(self,a):
        self.a = a
    def calcArea(self):
        self.area = self.a*self.a*6
    def calcVolume(self):
        self.volume = self.a*self.a*self.a
    def printInfo(self):
        print "Area : {0}, Volume : {1}".format(self.area, self.volume)

class Sphere(ThreeDim):
    r = 0
    def __init__(self,r):
        self.r = r
    def calcArea(self):
        self.area = 4*3.14*self.r*self.r
    def calcVolume(self):
        self.volume = 4/3*3.14*self.r*self.r*self.r
    def printInfo(self):
        print "Area : {0}, Volume : {1}".format(self.area, self.volume)

rec = Rectangle(2, 4)
rec.calcPerimeter()
rec.calcArea()
rec.printInfo()

tri = Triangle(3)
tri.calcArea()
tri.calcPerimeter()
tri.printInfo()

cir = Circle(5)
cir.calcArea()
cir.calcPerimeter()
cir.printInfo()

cub = Cube(4)
cub.calcArea()
cub.calcVolume()
cub.printInfo()

sph = Sphere(2)
sph.calcArea()
sph.calcVolume()
sph.printInfo()