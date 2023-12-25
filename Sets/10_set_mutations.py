
n = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command,length = input().split()
    elements = set(map(int, input().split()))
    if(command=="intersection_update"):
        A.intersection_update(elements)
    elif(command=="update"):
        A.update(elements)
    elif(command=="difference_update"):
        A.difference_update(elements)
    else:
        A.symmetric_difference_update(elements)
    
print(sum(A))

