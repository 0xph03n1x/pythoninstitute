#!/usr/bin/python3

x = int(input())
y = int(input())

x = x % y
print("First result: ", x)
x = x % y
print("Second result: ", x)
y = y % x

print(y)
