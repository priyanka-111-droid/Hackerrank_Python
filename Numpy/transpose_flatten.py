import numpy
N,M = map(int,input().split())
lst=[]
for _ in range(N):
    lst.append([int(x) for x in input().split()])
    
arr = numpy.array(lst)
print(numpy.transpose(arr))
print(arr.flatten())