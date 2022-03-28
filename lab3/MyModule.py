import math
from math import sqrt
class triangle:
    def __init__(self,x,y,z):
        self.x, self.y, self.z = x, y, z
    def surface(self):
        p = (self.x+self.y+self.z)/2
        return sqrt(p*(p-self.x)*(p-self.y)*(p-self.z))
    def circuit(self):
        return self.x + self.y + self.z
class square:
    def __init__(self, x):
        self.x = x
    def surface(self):
        return self.x * self.x
    def circuit(self):
        return 4*(self.x)
class circle:
    def __init__(self, r):
        self.r = r
    def surface(self):
        return (self.r * self.r) * math.pi
    def circuit(self):
        return 2 * (self.r) * math.pi
