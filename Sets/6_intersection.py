n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))

print(len(set(english.intersection(french)))) 