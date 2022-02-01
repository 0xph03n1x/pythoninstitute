#!/usr/bin/python3
def is_a_triangle(a, b, c):
    return a + b >c and b + c > a and c + a > b

a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle:
    print("Yes, it can be a triagnle.")
else:
    print("No, it can\'t be a triangle")