# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle_status(r):
    area= math.pi * (r**2)
    circumference= 2* math.pi * r
    return area, circumference

r = 5
area, circumference = circle_status(r)

print("Area:", round(area, 2))
print("Circumference:", round(circumference, 2))
