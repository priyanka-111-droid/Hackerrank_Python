from collections import deque

d = deque()


N = int(input())
for _ in range(N):
    value = input() 
    if(value.startswith("append")):
        operation,number= value.split()
    else:
        operation = value 
        
    if(operation=="append"):
        d.append(number)
    elif(operation=="appendleft"):
        d.appendleft(number)
    elif(operation=="pop"):
        d.pop() 
    elif(operation=="popleft"):
        d.popleft() 
        
print(*d)
    
