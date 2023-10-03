#!/usr/bin/env python3
entered_number = input("Please enter your number: ")
if entered_number.isdecimal():
    entered_number = int(entered_number)
    print("My number is " + str(entered_number))
    if entered_number >= 100:
        print("Your number is huge")
    elif entered_number < 0:
        print("Your number is negative")
    elif entered_number >10:
        print("Your number has two digits")
    else:
        print("Your number has one digit")
else:
    print("Sorry, you entered a non-integer character.")