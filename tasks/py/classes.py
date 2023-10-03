#!/usr/bin/env python3

class Person:
    objectcount = 0

    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        Person.objectcount += 1
        
    def compare(self, other):
        return self.height > other.height
    
person1 = Person("Beti", "Fabio", 24, 179)
person2 = Person("Mueller", "Hans", 67, 155)
print(Person.objectcount)

if person2.compare(person1):
    print(person2.name + " is older than" + person1.name)
else:
    print(person1.name + " is bigger than " + person2.name)


class Student:
    def __init__(self, name, age, grade, height):
        super().__init__()
        self.name = name
        self.age = age
        self.grade = grade
        self.height = height
        
    def compare(self, other):
        return self.grade > other.grade
    
yves = Student('Yves', 22, 5.5, 188)
leo = Student('Leo', 26, 4.6, 175)
print(yves.compare(leo))
print(person2.compare(yves))
print(yves.compare(person1))