'''
Input Format:
A single line containing the space separated string  and the integer value .
The string contains only UPPERCASE characters.

Output Format:
Print the permutations of the string  on separate lines.

Sample Input:
HACK 2

Sample Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

Explanation:
All possible size  permutations of the string "HACK" are printed in lexicographic sorted order.
'''

from itertools import permutations
a,b = input().split()
lst = sorted(["".join(tup) for tup in list(permutations(a,int(b)))])
print(*lst,sep="\n")

# "".join(tup) will concatenate all elements in a tuple