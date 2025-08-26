""""
count = 1
while count <= 10:
    print(count)
    count +=1

items = [1,2,3,4]

for index,item in enumerate(items):
    print(index,item)

"""
#-----------------------------
""""
class Animal:
    def walk(self):
        print("prowling....")


class Cat(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def meow(self):
        print("meowww!")

kitten = Cat("gerald",3)

print(kitten.name)
print(kitten.age)

kitten.meow()
kitten.walk()

"""

#----------------------------
"""
from dog import bark

bark()

"""

#----------------------------

""""
import math
import sys 

print(math.sqrt(3))
print(sys.argv)

"""
#-------------------------
""""

import argparse

parser = argparse.ArgumentParser(
    description='This program prints the name of dogs'
)
parser.addargument ('-c', '--color', metavar = 'color',required=True,choices = {'red','yellow'} ,help = 'the color to search for')

args = parser.parse_args()

print(args.color)

"""
#-------------------------
"""

lambda num : num * 2

multiply = lambda a,b : a* b

print(multiply(2,4))

"""
#-------------------------
"""
numbers = [1,2,3]

result = map(lambda a : a** 2 ,numbers)

print(list(result))

"""
#-------------
"""
numbers = [1,2,3]

def isEven(n):
    return n % 2 == 0

result = filter(isEven,numbers)

print(list(result))

"""
#---------------
"""
from functools import reduce
expenses = [('Dinner',100),('Fortnite',150)]
sum = reduce(lambda a, b: a[1] + b[1],expenses)

print(sum) 
"""
#------------------
"""
def factorial(n):
    if n ==1: return 1
    return n * factorial(n-1)

"""
#-----------------
"""
def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello")

hello()

"""
#----------------
"""
def increment(n :int) -> int:
    return n+1
print(increment(2))
"""
#------------------
"""
try:
    result = 67/0
except ZeroDivisionError:
    print("cannot do that sir")
finally:
    result = "math error"
print(result)

class DogNotFoundException(Exception):
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not FOund!!')

"""
#-------------------
"""
numbers = [1,2,3,4,5]

numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)

"""
#------------------
class Dog:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def __gt__(self,other):
        return True if self.age > other.age else False
    
dog1 = Dog("james",17)
dog2 = Dog("jenni",18)
print(dog2>dog1)