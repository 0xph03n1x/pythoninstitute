#!/usr/bin/python3

from email.errors import FirstHeaderLineIsContinuationDefect


def introduction(first_name, last_name="Smith"):
    print("Hello my name is", first_name, last_name)

#defining last_name overrides the default parameter value
introduction("James", "Doe")

#defining only first parameter
introduction("Henry")
introduction("William")

#having default values on both parameters
def introductions(first_name="John", last_name="Smith"):
    print("Hello my name is", first_name, last_name)
introductions()
introductions(last_name="Hopkins")