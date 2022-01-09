#!/usr/bin/python3

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
mins = mins + dura
hour = hour + mins // 60
print(hour % 24, ":", mins % 60, sep = "")
