T = int(input())
for _ in range(T):
    try:
        a,b = map(int,input().split())
    except ValueError as v:
        print("Error Code:",v)
        
    else: 
        try:
            print(a//b)
        except ZeroDivisionError as z:
            print("Error Code:",z)
        