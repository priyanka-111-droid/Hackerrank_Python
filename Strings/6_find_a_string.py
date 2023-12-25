def count_substring(string, sub_string):
    window_len =len(sub_string)
    window_start = 0
    window_end = window_len-1
    count=0
    for _ in string:

        # for only valid index,
        if window_start>=0 and window_end<len(string):
            window = string[window_start:window_end+1]
            if(window==(sub_string)):
                count+=1
            
            #always shift window ahead.
            window_start+=1
            window_end+=1
        else:
            break
    return count
# like sliding window problem 




#way 2 - 
# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count