import calendar

month, day, year = map(int, input().split())
weekday = calendar.weekday(year, month, day) # gives integers(eg. 0 for Monday)
day_name = calendar.day_name[weekday] #converts integer to day name
print(day_name.upper()) #need to print day name in upper case

