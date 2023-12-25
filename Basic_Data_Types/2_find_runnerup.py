n = int(input())
nums =list(map(int,input().split(' ')))
print (list(sorted((set(nums))))[-2])

# we can use map or list comprehension to take user input separated by space.Here we have used map
# Convert nums list to set so that all duplicates are removed.
# Then sort it in asc order,convert to list and pick 2nd last element.
# 2nd last element or 2nd element from right is the runner up.