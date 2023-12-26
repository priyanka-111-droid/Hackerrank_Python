'''
Task
You are the manager of a supermarket.
You have a list of  items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format:
The first line contains the number of items, .
The next  lines contains the item's name and price, separated by a space.

Output Format:
Print the item_name and net_price in order of its first occurrence.

Sample Input:
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output:
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''

# We are using ordered dict since we need to print the item_name and net_price in order
# of its FIRST OCCURENCE.Ordered dict remembers the order of the keys that were inserted first. 
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.

from collections import OrderedDict
ordinary_d=OrderedDict()

N = int(input())
for _ in range(N):
    values = input().split()

    if len(values)==3: # in case item name has 2 words. eg. BANANA FRIES
        item_name = values[0]+" "+values[1]
        price = int(values[2])
    else: #in case item name has 1 word.Eg. CANDY
        item_name = values[0]
        price = int(values[1])
    
    #input into a dictionary
    if item_name in ordinary_d.keys(): #if item name already exists among dictionary keys,
        ordinary_d[item_name]+=int(price)# add price of that item since we need net price of each item.
    else:
        ordinary_d[item_name] = int(price)#if item does not exist, input item name as dictionary key and record price of item as dictionary value.
        
for key in ordinary_d.keys():
    print(f"{key} {ordinary_d[key]}")