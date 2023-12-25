# Hackerrank Python Solutions (Topic wise)

Hackerrank Python solutions done topic wise. Tricky solutions are explained and multiple solutions are mentioned if applicable.

## Important Tips Topic-wise

### Introduction

- Can also input multiple numbers like this(when numbers entered on new line) : a,b= [int(input()) for _ in range(2)]

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