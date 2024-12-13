
# string - strings are stored in either single quote or double quotes '' or ""

name = "Ram's"

multiline = '''Hi everyone
I am Niraj
thank you'''
print(name)
print(multiline)
print(type(name))

# Integer - Integer datatypes are use to define numbers  eg
num1 = 1 #this is an integer datatype

# Float - float is used to define fractional number
num2 = 1.5

# sequential datatype(Group datatypes)

# List datatypes - ordered datatype, mutable denoted by []
a = ["apple","Banana",[1,2,3]]
print(type(a))
print(a)
a.pop()
a.append("Ram")
print(a.index("apple"))
print(a)
# Tuples - ordered datatypes , immutable denoted by ()

b = ("apple","Banana",1,2)
print(type(b))

# Sets - unordered datatype denoted by {}

c = {"apple","ball","a","a"} #can be used to filter duplicate values

# Dictionaries - denoted by {} stored in key-value pairs

dictionary = {
    "name":"niraj",
    "age": 23,
    "address":"ktm"
}

# Boolean - either true or false

IsHome = True

# None datatype
var = None

print(type(var))
