import numpy

lst = [x for x in input().split()]
arr = numpy.array(lst,int)
arr.shape = (3,3)
print(arr)
