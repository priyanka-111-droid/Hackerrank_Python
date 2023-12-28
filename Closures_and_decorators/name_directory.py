import operator

def person_lister(f):
    def inner(people):
        # complete the function
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# - The key parameter in the sorted function should be a function, 
# Need to  pass a lambda function that takes a person 
# and returns the value by which the list should be sorted. 

# - The name_format function should return a list of formatted names for all people, 
# Have to use a list comprehension to apply the formatting to each person.