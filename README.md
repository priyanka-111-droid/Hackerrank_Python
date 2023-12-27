# Hackerrank Python Solutions (Topic wise)

Hackerrank Python solutions done topic wise. Tricky solutions are explained and multiple solutions are mentioned if applicable.

## Important Tips Topic-wise

### Introduction

- Can also input multiple numbers like this(when numbers entered on new line) : a,b= [int(input()) for _ in range(2)]
- input N and X separated by space(N,X are integers): N,X = map(int,input().split())

### Basic Data Types

### Strings

### Sets

- Update,Union,Intersection,Difference
- add
- remove,discard,pop
- set mutations - A.update(B),A.intersection_update(B)

### Math

- Complex numbers-> cmath module
    - Convert a+bj form to complex number z using complex()
    - Convert complex number z to polar coordinates:r and phi
    - r: abs(complex(z))
    - phi: cmath.phase(complex(z))

- It's also possible to calculate pow(a,b,m)  

### Itertools

- itertools.product - combination of cartesian products.
```
 print(*(list(itertools.product(A,B)))) # * will print all elements in the list.
```
- itertools.permutations

### Collections

- counter
- Data = namedtuple('Data', columns)
- OrderedDict: An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

### Date and Time
- calendar.weekday(year, month, day)
- datetime.strptime(timestamp, format)


### Errors and Exceptions
- Exceptions -> Errors detected during execution
- Exception handling with try,catch,else,finally:
Try: This block will test the excepted error to occur
Except:  Here you can handle the error
Else: If there is no exception then this block will be executed
Finally: Finally block always gets executed either exception is generated or not
- import re(regex library)

### Classes

### Built Ins

- eval keyword usage
- zip function 
- EOF Error
- sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))

### Functionals
- map
- reduce
- re.match for emails

### XML


### Closures and Decorators

### Numpy

### Debugging