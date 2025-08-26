# tutorial
contains the tutorial i followed to learn the basics of python for my NEA.

https://www.youtube.com/watch?v=eWRfhZUzrAc&ab_channel=freeCodeCamp.org

currently: 2:23:03

In my read me I will take the notes I learned from the video. 

# <ins> RPS first example </ins> #
# 1 #
dictionaries are a useful way to store different data that correlate to something. The usage can vary, as long as you have a key that can be used later on in the program.

the syntax for a dictionary is {}, with a : seperating a key and the value correlated to it. 
dictionary = {"name":"james"}
# 2 #
lists have a standard syntax. 
lst = ["james","jenni","merida"]

# 3 #
fstrings are also useful when you want to format strings that include variables.
For example, "james is " + age + "years old" can become
f"james is {age} years old"

# <ins> going through different stuff (examples.py) </ins> #

# 1 #
isinstance is a cool function that checks if something is a specific data type.
For example, you'd pass a variable into the function, and then a data type and it will return the boolean value.
isinstance("james",str)   would return True.
you can use it on 'complex' numbers, bool, list, tuple, range, dict and set.

# 2 #
strings have useful functions to manipulate strings
len() gets the length of the string
lower() makes it lowercase
upper() uppercase
title() makes the first letter capitalised for each word 
isalpha() checks if it only contains characters (not empty)
isdecimal() checks if only digits (not empty)
isalnum() checks if contains characters or digits (not empty)
startswith() self explanatory
endswith() self axplanatory
split() splits a string by a specific character
a \ allows the next character to escape the string. You could then add a " for example to a string
"Jam\"es"

string slicing allows you to select specific indexes of a string using substring and different manipulation techniques
name = "James"
print(name[1:2]) would return 'a'

# 3 #
Booleans are similar to C, very simple

you can assign variables with boolean values like 'True' and 'False'
the Integer 0 refers to False, all others return True
similar with strings, an empty string is False, otherwise True

all is useful function to check if all the values in a list or dict are True.

# 4 #
complex numbers may be useful for complex mathematical programs, and using the character 'j' refers to the imaginary part of the number.
for example, num = 2 + 3j would be a complex number where 3 is imaginary

you could also do this through the function 'complex()'
num = complex(3,4)

print(num.real,num.imag)

'abs' is a useful function to return the absolute value of a number, essentially returning the positive value of any number.
round has a similar effect. it just rounds to the nearest number. 

Enums are readable names bound to constant values. Python is unique, there's no way to set constants in base python unlike other languages like C, so we can use libraries like Enum.

# 5 #

input statements are very easy to understand, you just use the function
'input' to get the users input, which will wait till the enter key is entered by the user.

# 6 #
lists are very useful when solvign problems that require data storage that may be related. there are many functions for list manipulation

[] are used to gert specific elements in a list 
append allows you to add 1 element to the list, but
extend allows you to add multiple elements to a list, like combining 2 lists together
you could also just use '+=', which has the same function as extend.
'remove' is used to remove a specific element from a list
'pop' is similar, except it removes the last element from a list, like removing the top of a stack.
'insert' is useful if you want to place an element in a specific index for a list. 

'sort' allows you to sort a list, digits become sequential, while strings are sorted alphabetically, capital letters first.
However, you can set custom keys to sorts, if you want it to sort lowercase too.
you can also print a list that's sorted without actually modifying the list using a function called 'sorted'

# 7 # 
tuples are similar to lists, except you cant modify them  at all; this means you cannot add to them or remove elements from them.
They're also ordered automatically.

you create them using () instead of []

you are able to add a tuple to a new tuple upon instantition, because that doesn't count as manipulating the original tuple

# 8 #
dictionaries use keys and values to store a literal dictionary of data.
There will a key you can call which will return what it is storing.

you can use a function called 'get' to return the value of a key in a dict.
'pop' will return the item you deleted, but then delete it from the dictionary via the key that you passed into it.
'popitem' is similar, it just removes the last key and value that was added to the dictionary.
using dict.'keys' will return a list of all the keys for a dictionary. This is the same for 'values' which returns a list of the values in a dictionary.
'items' will just return everything in the dictionary as a list.

You can very easily add an item but using square brackets, which contains the key and then the a '=' followed by the value.

names["Jenni"] = 18

the 'copy' function just copies a dict to a new variable name

# 9 #

sets have similar syntax to dictionaries, but they dont use colons, they are just unchangeable, lists that dont allow duplicates.

the '&' sign will return what element is common between 2 sets
'|' will tell you every item in two sets (no duplicates tho)

you can use signs like -,< > to see what's the difference between 2 sets or to see which set contains all of the other set.

# 10 #

functions are very useful for readability and maintainablity of a program. It also allows repitition of code very easily!

functions do not typically change the value of a variable outside the function (ignore passing by ref and value at the moment), but dictionaries are mutable, meaning they will be effected if you change it within a function.

you are able to return multiple things from a function by seperating them using a ','
its important to consider variable scope for functions, as some can have a global scope, while some have a local scope (only changeable within that function).
to access a variable which is local in a function that doesn't have it as a parameter, you can use something called 'nonlocal' to access that variable inside a non local scope. 

you are also able to use nested functions if you wish to do repition within the parent function.
If you use nested functions, and you wish to call the nested function, you can do so, without doing the previously lines of code before that function is instantiated. This is useful because the parent function may reset a variable to 0, which you dont want to do.

# <ins> OOP + more stuff (OOP.py) </ins> #

# 1 #

objects of course have attributes and methods.
Every data strcuture is an object in python; lists, tuples and dictionaries are all objects.
This means manipulating them is nothing different from what we have learnt already.

# 2 #

classes are used to create a template. You can then instantiate classes as objects, which take up the template/skeleton created within the class.

you can use __init__(self, ...) to create a costructor for a class. Whenever you create a variable too that is within the class you should preface it with 'self.' to show it is the variable within that class.

Similar to learning OOP in Java, you can use parent classes and child classes to inherit different methods.

# 3 #

Modules in python are just files which can be imported into different files so they can be accessed and used. What you can do is import python files by simply adding 'import x' where x is the name of the file to gain any functions defined in that module.
If you then have a folder that you want to use but the main file is outside the folder, you can add a __init__ file to the folder, allowing you to do something like 'from lib import x'.'
If you want to call a specific function, you can call from lib.x import fight' where fight is the name of the function and x is the name of the python file.
There are a lot of standard libraries you can import from, which you can find online.
Some common ones are:
json, math, random, os, statistics, http, and urllib.

# 4 #

lambda functions are used to create simply arithmetic functions, which you can then use later on in your program. They can also be used with map,filter and reduce.

# 5 #

map is used to run a function upon each item in a datastructure, like a list, that can then be manipulated and changed, which can be very useful for different problems.
You can easily do this with lambda functions, as the function that doubles or squares a number can be written as a lambda function.

filter is a function that takes a 'filtering' function and a list, and based on the return value (True or False) for the item in the list, the list will be changed. 

reduce functions are used to find the sum of a list of something. It creates a shorthand/quicker way to create a loop that would sum digits in a list.

# 6 #

recursion in python is similar to any other language, you just follow python syntax. It is very useful for intuitive and basic programming as long as the stack doesn't overflow due to too many functions being called.

# 7 #

decorators in python are ways to change how a function works. This done using the '@' symbol. This could be useful if you want to do analysis for a function, or if you wish to alter how it works without directly changing the function.

# 8 #

docstrings are just a different form of a comment that has a different look to it.

"""Hello, i am a docstring """

These are actually useful becuase if you run 
print(help(x)) where x is a class, itll print all the other docstrings writen in that class to help you understand its function!

# 9 #

annotations are a useful way of writing down what a function should do, as you can specificy the data type that it should take in and return.

# 10 #

exceptions are useful, sort of like an if else statement. You can put somethin in the try block, and if that happens the exception will be called, preventing a logic error that prevents the user from progressing or understanding what happened.

# 11 #

pip is essential if you want to create a complex program, as different packages/libraries are avialable to download through using pip. 

you can do 'pip install x' where x is the package you wish to install.
Once something is installed, you can import it into your python files for your own use!

# 12 #

list compressions are a way to create lists very concisely.
it's a very specific syntax, sort of like mapping functions, where you can copy a list but do a function on it.

# 13 # 
operator overloading is used to compare two objects within the same class together. It uses a __gt__ function, where different attributes can be entered and compared.
'gt' is only used to for the greater than operator, but there are many different function names you can use for different functions like 
__mod__ for the % operator
__mul__ for the * operator
__lshift__  for the << operator (left shits the bits by x places)
__and__ for the & operator
__or__ for the | operator