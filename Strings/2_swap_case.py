def swap_case(s): 
    result = ''
    for i in s:
        if i.islower():
            result += i.upper()
        else:
            result += i.lower()
    return result




#shorter way - 
# def swap_case(s):
#     return s.swapcase()

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)