from enum import Enum
#this file just contains the different example he goes through and me doing them with him
name = "james"
age = float(18)  # this casts age to a float over an integer. 
#this is a comment!
#print(name)
#print(isinstance(name,str))

4 % 3 #1 MODULO
4**2 #16 power symbol
5//2 #2 floor division

number = 12
number **= 2 #144

c1 = True
c2 = False
c1 and c2 #false
c1 or c2 # true

#---------------------------------------

name = "James"
name += " Cook"

#print(name.lower())
#print(name.isalpha())

name += "\""
#print(name)
name = "James"
#print(name[1:2])

check = True
#print(type(check) == bool)

#---------------------------------------

num3 = complex(3,4)

#print(num3.real,num3.imag)

#print(abs(4.32))
#print(round(3.2))

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

#print(State.ACTIVE.value)

#---------------------------------------

#age = input("what is your age:")
#print("Age:" + age)

#---------------------------------------

condition = False
if(condition == True):
    print("condition is trueeeee")

#---------------------------------------

""""
myList = ["James", "Jenni", "Oscar", "Raffe"]

print(myList[3])
print(myList[:4])
myList.extend([3,4,"HULK SMASH"])
myList.remove(3)
print(myList)
myList.insert(0,"im number 1")
print(myList)

lst = [1,5,35,32,63,21]

lst.sort()
print(lst)

newLst  = ["James", "Oscar", "Jenni", "Raffe"]

print(sorted(newLst))
print(newLst)
newLst.sort(key=str.lower)
print(newLst)

names = ("James","Wood","Mayed","Adam")

print(len(names))
print("James" in names)

"""
#---------------------------------------

"""
james = { "name": "James", "age": 18, "country": "England"}

print(james.get("name"))
print(james.pop("country"))
print(james)
print(james.keys())
print(james.values())
print(james.items())

"""

#---------------------------------------

set1 = {"James","Jenni"}
set2 = {"Jenni"}

print(set1 - set2)
print(set1 | set2)
print(set1 > set2)

#---------------------------------------

dict5 = {"name":"James","age": 18}
def change(dict):
    dict["name"] = "James Cook"

change(dict5)
print(dict5)

def wordByWord(sentence):
    def say(word):
        print(word)
    
    words = sentence.split(' ')
    for word in words:
        say(word)

wordByWord("My name is James Cook")
