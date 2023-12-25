'''
You are given three integers: , , and . Print two lines.
On the first line, print the result of pow(a,b). 
On the second line, print the result of pow(a,b,m).
'''

a,b,m = [int(input()) for _ in range(3)]
print(pow(a,b))
print(pow(a,b,m))