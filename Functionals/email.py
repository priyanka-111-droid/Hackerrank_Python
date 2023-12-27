import re
def fun(s):
    # return True if s is a valid email, else return False
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    
    #returning the email adress
    return(a)


# re.match() searches only from the beginning of the string and return match object if found. 
#But if a match of substring is found somewhere in the middle of the string, it returns none. 
#re.search() searches for the whole string even if the string contains multi-lines 
#and tries to find a match of the substring in all the lines of string.