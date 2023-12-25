'''
Task:
You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format:
A single line containing the string  and integer value  separated by a space.
The string contains only UPPERCASE characters.

Output Format:
Print the different combinations of string  on separate lines.

Sample Input:
HACK 2

Sample Output:
A
C
H
K
AC
AH
AK
CH
CK
HK
'''
from itertools import combinations
s,k = input().split()

for i in range(1,int(k)+1):
    lst = sorted(["".join(tup) for tup in (list(combinations(sorted(s),int(i))))])
    print(*lst,sep="\n")
    
