#!/usr/bin/python3
def strange_list_func(n):
    strange_list = []
    for i in range (0, n):
        strange_list.insert(0, i)
    return strange_list

print(strange_list_func(5))