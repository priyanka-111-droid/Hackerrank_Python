'''
Input Format
The first line contains an integer, , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.

Output Format:
Output the total number of students who have at least one subscription.
'''

n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))

print(len(set(english.union(french)))) 