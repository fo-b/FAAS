#!/usr/bin/env python3
import math

# faculty with for
def facultywithfor(n: int):
    y = 1
    if n >= 2:
        for i in range(2, n + 1): 
            y = y * i
    return y


print(facultywithfor(7))

# faculty with while
def facultywithwhile(n: int):
    y = 1
    i = 2
    while i <= n:
        y = y * i
        i += 1
    return y

print(facultywithwhile(5))

def fibonacci_rule(n: int):
    if n == 0:
        return 0
    x = 1  
    xx = 0
    z = 1
    i = 3
    while i <= n:
        xx = x
        x = z
        z = x + xx
        i += 1
        return z
    
print(fibonacci_rule(0))
print(fibonacci_rule(1))
print(fibonacci_rule(2))
print(fibonacci_rule(3))
print(fibonacci_rule(4))
print(fibonacci_rule(5))
print(fibonacci_rule(6))

def numfilter(list: list):
    sum = 0
    for element in list:
        if type(element) == float or type(element) == int:
            sum += element
    return sum


print(numfilter([44, 32.3, "cc", "puup", "77.5"]))

def numonlyfilter(list: list):
    sum = 0
    for element in list:
        if not (type(element) == float or type(element) == int):
            continue
        if element < 0:
            break
        sum += element
    return sum

print(numonlyfilter([44, 32.3, "cc", "puup", "77.5", 4, 99, -25]))

def numprime(num: int) -> bool:
    dff = int(math.sqrt(num))
    i = 2
    while i <= dff:
        if num % i == 0:
            return False
        i += 1
    return True