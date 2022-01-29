#!/usr/bin/python3
def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([5, 4, 3]))
#print(list_sum(5))      #doesn't work since single value cannot be iterated by the for loop