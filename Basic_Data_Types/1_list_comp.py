import itertools
if __name__ == '__main__':
    x,y,z,n=[int(input()) for _ in range(4)]
    ansx=[x1 for x1 in range(0,(x+1))]
    ansy=[y1 for y1 in range(0,(y+1))]
    ansz=[z1 for z1 in range(0,(z+1))]
    ans=[ansx,ansy,ansz]
    print([list(i) for i in (itertools.product(*ans))if sum(i)!=n])

    #here itertools.product(*ans) gives cartesian product(tuples) of all iterables ansx,ansy and ansz.
    #We pick the tuples whose sum does not equal to n and convert it to a list.
    # Then we add it to a bigger list holding many such smaller lists.
    





# way 2 - better way without itertools and without creating 3 separate lists 
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
# code = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
# print(code)

