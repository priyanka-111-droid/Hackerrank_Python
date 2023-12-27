'''
Task
You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).
NOTE: Python2 users, please import from __future__ import print_function.

Constraint:
Input string is less than 100 characters.

Sample Input:
print(2 + 3)

Sample Output:
5
'''

st = input()
(eval(st)) 
# if we do print(eval(st)), output will be 5 and then None on next line, since print is an impure function
# It will display None as a side effect.

'''
Eval keyword usage->
>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
>>> type(eval("len"))
<type 'builtin_function_or_method'>
'''