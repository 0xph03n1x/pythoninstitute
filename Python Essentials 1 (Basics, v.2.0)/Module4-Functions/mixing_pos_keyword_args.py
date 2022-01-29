#!/usr/bin/python3

from audioop import add


def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)    

adding(5, 6, 7)     #positional variant
adding(c = 7, a = 5, b=6)       #keyword variant
adding(5, c= 7, b = 6)      #mixed variant
adding(5, 6, c = 7)     #mixed variant