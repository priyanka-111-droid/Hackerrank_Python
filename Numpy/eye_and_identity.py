import numpy


numpy.set_printoptions(legacy='1.13') # to make alignment and spacing proper.
N,M = map(int,input().split())
print(numpy.eye(N,M,k=0)) #k=0 means main diagonal(default value)
