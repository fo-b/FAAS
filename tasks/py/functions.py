#!/usr/bin/env python3

def powar(base, exponent=1):    
    return base ** exponent     


print(powar(2, 10))      

print(powar(exponent=10, base=2))       

print(powar(10))                     

def stringconcat(*arguments):          
    result = ""                         
    for arg in arguments:               
        result += str(arg) + " "       
    return result

print(stringconcat("dddd", 1, 3.4, [1, 3], int, float, str))

def print_table(title, **keyvalue):    
    print(f"{title:100s}")               
    print("-" * 100)                          
    print(f"{'key':20s} | {'value':67s}")       
    print("-" * 100)                            
    for k, v in keyvalue.items():              
        print(f"{str(k):20s} | {str(v):67s}")  


print_table("test_table", number=12123, string="Hello");
