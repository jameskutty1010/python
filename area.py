#!/usr/bin/python3
PI = 3.14
r = float(input("Radius of the circle: "))
if (r < 0):
    print("unsupported value")
else:    
    A = PI * r * r
    print("Area of circle: %f" %A)
