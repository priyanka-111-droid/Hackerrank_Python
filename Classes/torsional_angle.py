import math

class Points(object):
    def __init__(self, x, y, z): #every point A,B,C,D each has 3 coordinates - x,y,z
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        v1, v2 = (self.x, self.y, self.z), (no.x, no.y, no.z)
        return Points(*[i - j for i, j in zip(v1, v2)])
        
    def dot(self, no):
        v1, v2 = (self.x, self.y, self.z), (no.x, no.y, no.z)
        return sum([i*j for i, j in zip(v1, v2)])
        
    def cross(self, no):
        res = self.y * no.z - self.z * no.y, self.z * no.x - self.x * no.z, self.x * no.y - self.y * no.x
        return Points(*res)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)