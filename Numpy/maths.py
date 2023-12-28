import numpy


try:
    N, M = map(int,input().split())
    A = numpy.array([input().split() for _ in range(N)], dtype = int)
    B = numpy.array([input().split() for _ in range(N)], dtype = int)
    print(A+B,A-B,A*B,numpy.floor_divide(A,B),numpy.mod(A,B),numpy.power(A,B), sep ='\n')
    
except EOFError as e:
    pass


# another way:
# import numpy
# try:
#     N, M = map(int,input().split())
#     A = numpy.array([[(x) for x in input().split()] for _ in range(N)], dtype = int)
#     B = numpy.array([[(x) for x in input().split()]for _ in range(N)], dtype = int)
#     print(A+B,A-B,A*B,numpy.floor_divide(A,B),numpy.mod(A,B),numpy.power(A,B), sep ='\n')
    
# except EOFError as e:
#     pass