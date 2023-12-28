N = int(input())
lst = [int(x) for x in input().split()]
isPal = lambda x: str(x)==str(x)[::-1] 
print(all(x>=0 for x in lst) and any(isPal(x) for x in lst))# 'and' because both conditions have to be True


# Example:
# we want to verify is every element in l is even by using the All method.
# all(x % 2 == 0 for x in l)
# check if Any of the elements in l is odd by using the Any method.
# print(any(x % 2 != 0 for x in l))
