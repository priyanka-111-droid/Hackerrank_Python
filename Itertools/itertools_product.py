'''
Input Format:
The first line contains the space separated elements of list .
The second line contains the space separated elements of list .
Both lists have no duplicate integer elements.

Output Format:
Output the space separated tuples of the cartesian product.

Sample Input:
 1 2
 3 4
Sample Output:
 (1, 3) (1, 4) (2, 3) (2, 4)
'''

import itertools
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(*(list(itertools.product(A,B))))
