#!/usr/bin/env python3
input_string = input("Enter a string: ")
vowel_count = 0
vowels = "aeiouAEIOU"
for char in input_string:
    if char in vowels:
        vowel_count += 1
print("The total number of vowels in the string is:", vowel_count)