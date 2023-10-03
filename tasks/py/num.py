#!/usr/bin/env python3
entered_number = input("Please enter your number: ")
if entered_number.isdigit():
    entered_number = int(entered_number)
    print("My number is " + str(entered_number))
else:
    print("Sorry, you entered a non-integer character.")