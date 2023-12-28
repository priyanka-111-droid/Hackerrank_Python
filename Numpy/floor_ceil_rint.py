import numpy

numpy.set_printoptions(legacy='1.13')
arr = numpy.array(
   [x for x in input().split()],float
)
print(numpy.floor(arr),numpy.ceil(arr),numpy.rint(arr),sep="\n")