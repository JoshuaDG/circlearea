import math

class Circle:
    def __init__(self,rad):
        self.radius = rad
    def calc_area(self):
        area = self.radius* 2 * math.pi
        return area
    def calc_perim(self):
        perim = 2 * self.radius * math.pi
        return perim
        
cir = Circle(5)
area = cir.calc_area()
print("Area is %.3f" % area
