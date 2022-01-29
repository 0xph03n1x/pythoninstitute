#!/usr/bin/python3
#return without an expression

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year!")


happy_new_year(False)
