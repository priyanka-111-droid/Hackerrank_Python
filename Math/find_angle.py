'''
ABC is a right triangle,  at .
Therefore, Angle ABC is 90.
Point  is the midpoint of hypotenuse .
You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.
'''
import math

AB = int(input())
BC = int(input())
AC = math.sqrt(math.pow(AB, 2) + math.pow(BC, 2))
MC = AC / 2.0

theta = math.atan(AB / BC)
angle_in_degrees = math.degrees(theta)
rounded_angle = round(angle_in_degrees)

print(str(rounded_angle) + u'\N{DEGREE SIGN}')


# Forget about M. Since ABC is a right triangle and M = AC/2, 
# the MBC is an isosceles triangle, which means that angle B and 
# angle C in MBC will always be equivalent so just find C. 
# Since the goal is to find an angle, and we have adjacent and opposite sides, 
# just use the attangent of C.
