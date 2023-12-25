'''
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.
Find the total number of distinct country stamps.

Sample Input:
7
UK
China
USA
France
New Zealand
UK
France

Sample Output:
5

Explanation:
UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).
'''


N = int(input())
district=set()
while(N):
    district.add(input())
    N-=1
    
print(len(district)) #set will not store duplicates,so length of set gives number of elements.