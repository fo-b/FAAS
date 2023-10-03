#!/usr/bin/env python3
def print_type(inputlist: list):
    for element in inputlist:
        print(type(element))
        print(str(element))

print_type(["Fabio", 23,0.6,1999])

def find(inputlist: list, lookelement):
    index1 = []
    for i in range(0, len(inputlist)):
        if inputlist[i] == lookelement:
            index1.append(i)
    return index1
list3 = ["Fabio", 12, 222, 8, "somethinf", 69]
print(find(list3, 69))

def containnum(numlist: list):
    for element in numlist:
        if not (type(element) == int or type(element) == float):
            return False
        return True
    
print(containnum(["Upps", 22, 55]))
print(containnum([22, 55, 88, 99, 7.8]))