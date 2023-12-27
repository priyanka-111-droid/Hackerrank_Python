s = input()
l,u,odd,even=[],[],[],[] #4 lists initialized
for char in s:
    if char.islower():
        l.append(char)
    elif char.isupper():
        u.append(char)
    else:
        if int(char)%2!=0:
            odd.append(char)
        else:
            even.append(char)
            
print("".join((sorted(l)+sorted(u))+sorted(odd)+sorted(even))) #"".join will convert the combined list to string.

#better way:
# s = input()
# result = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))
# print(''.join(result))

#Explanation ->
# sorted sorts elements based on the key.
# tuples are sorted such that False is ordered before True
# Check this for details: https://stackoverflow.com/questions/75714886/cant-understand-the-lambda-function-inside-the-sorted-key-argument

