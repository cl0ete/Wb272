class Line(object):
    def __init__(self,coor1,coor2):
        self.one = coor1
        self.two = coor2
    def distance(self):
        return ((self.two[0]-self.one[0])**2+(self.two[1]-self.one[1])**2)**0.5
    def slope(self):
        return (float((self.two[1]-self.one[1]))/(self.two[0]-self.one[0])
    def __str__(self):
        return "coor1={1} and coor2={2}".format(self.one,self.two)


class Cylinder(object):
    pi = 3.14
    def __init__(self,height, radius):
        self.h = height
        self.r = radius
    def volume(self):
        a = (pi*self.r**2)*self.h
        return a
    def surface_area(self):
        a = ((pi*self.r**2)*2)*((2*pi*self.r)*self.h)
        return a
