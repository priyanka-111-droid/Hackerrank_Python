'''
You are given a string .
Your task is to find out whether  is a valid regex or not.
'''


#only works with Pypy

import re 

T = int(input())
for _ in range(T):
    s=input()
    try:
        re.compile(s)
        is_valid=True
    except re.error:
        is_valid=False 
    print(is_valid)


