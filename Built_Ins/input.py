#can be done on Python3 or Pypy too
'''
Sample Input:
1 4
x**3 + x**2 + x + 1

Sample Output:
True

Explanation: If you substitute x with 1 in polynomial equation, you get 4.
'''
x, k = map(int, input().split())
print(True) if eval(input()) == k else print(False) #input() takes in P polynomial