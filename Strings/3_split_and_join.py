def split_and_join(line):
    # write your code here
    return "-".join(line.split()) #will first split string into list and then will join items in list by '-'

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)