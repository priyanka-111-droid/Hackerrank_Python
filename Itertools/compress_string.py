from itertools import groupby
S = input()
result = [(len(list(v)), int(i)) for i, v in groupby(S)]

print(*result)