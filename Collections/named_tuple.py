from collections import namedtuple

N=int(input())
columns = [x for x in input().split()]
Data = namedtuple('Data', columns)
total_marks=0
for _ in range(N):
    values = [x for x in input().split()]
    each_student = Data(*values)
    total_marks = total_marks+int(each_student.MARKS)
print(f"{(total_marks/N):.2f}")