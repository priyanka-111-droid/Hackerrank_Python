def mutate_string(string, position, character):
    #strings are immutable in python
    
    #way 1 - Use replace.
    # new_string = string[:position]+ string[position:].replace(string[position],character,1)
    # Here,part of string before position is kept as it is and from position onwards, we will replace char at position with new character.We have added 1 so that only first occurence of char is changed.

    # way 2 - Use slicing (easier)
    new_string = string[:position]+ character+ string[position+1:]
    return new_string
   

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)