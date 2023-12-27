import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        

    def __sub__(self, no):
        return Complex(self.real -no.real, self.imaginary -no.imaginary)
        
        
    def __mul__(self, no):
        #(a + ib) (c + id) = (ac - bd) + i(ad + bc).
        return Complex(self.real * no.real - self.imaginary * no.imaginary, self.real * no.imaginary + self.imaginary * no.real)
        

    def __truediv__(self, no):
        return Complex((self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2), (self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2))

    def mod(self):
        k = math.sqrt((self.real ** 2) + (self.imaginary ** 2))
        return Complex(k,0)
    

'''
double underscore methods are builtin methods in Python. Can be used for operator overloading.
__add__-> Can be overloaded for + operation

__sub__ -> Can be overloaded for - operation

__mul__ -> Can be overloaded for * operation
'''