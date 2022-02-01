#!/usr/bin/python3

#Recursion in fibonacci example
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

#Recursion in factorials example
def factorial_func(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_func(n - 1)
    