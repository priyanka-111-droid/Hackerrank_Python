'''
Given  sets of integers,  and , print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either  or  
but do not exist in both.

Input Format:
The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.
'''

m = int(input())
setm = set(map(int,input().split()))
n = int(input())
setn = set(map(int,input().split()))
combined = sorted((setm.difference(setn)).union(setn.difference(setm))) #can also do union of setm,setn - intersection of setm,setn
# print("\n".join([str(x) for x in combined]))
#join can only be done on str(x) not on ints

print(*combined,sep="\n") #better way to write above


