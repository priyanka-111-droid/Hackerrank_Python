# Complete the solve function below.
def solve(s):
    temp= s.strip().split(" ")
    s1=[]
    for x in temp:
        s1.append(x.capitalize())
    return (" ".join(s1))
        