'''
Task:
You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis 0.

Input Format:
The first line contains space separated integers N,M  and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format:
Print the concatenated array of size X.

Sample Input:
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

Sample Output:
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
'''
import numpy
N,M,P = map(int,input().split())
arr1 = numpy.array(
    [[int(x) for x in input().split()] for _ in range(N)]
)
arr2 = numpy.array(
    [[int(x) for x in input().split()] for _ in range(M)]
)
print(numpy.concatenate((arr1, arr2)))

# better way
# import numpy as np
# N, M, P = list(map(int, input().split()))
# arr1 = np.array([input().split() for _ in range(N)], dtype='int')
# arr2 = np.array([input().split() for _ in range(M)], dtype='int')
# print(np.concatenate((arr1, arr2), axis=0))