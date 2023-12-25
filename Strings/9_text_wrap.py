

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
        #"".join(<LIST>) will convert list items to string
        #\n will make sure each string is printed on new line


