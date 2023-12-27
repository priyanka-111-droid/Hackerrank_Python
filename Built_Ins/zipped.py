'''
Input Format:
The first line contains  and  separated by a space.
The next  lines contains the space separated marks obtained by students in a particular subject.

Output Format:
Print the averages of all students on separate lines.
The averages must be correct up to  decimal place.

Sample Input:
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Sample Output:
90.0 
91.0 
82.0 
90.0 
85.5        
'''
N,X = map(int,input().split())
marks=[]
try:
    for _ in range(X):
        each_student = list(map(float,input().split()))
        marks.append(each_student)

    print(*[sum(tup)/X for tup in ((zip(*marks)))],sep="\n")
    # sum(tup)/X calculates average
    # * used to unpack elements in list(access each individual element in list)
    # sep="\n" ensures each element of list on new line.

except EOFError as e: #to ensure no EOF error.
    pass

        
        