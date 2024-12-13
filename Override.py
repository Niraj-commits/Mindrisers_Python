

var1 = "Hello"
var1 = "World" #overrides the value of variable "var1"
print(var1)
print(var1[0])
print(var1[0:3])

# Indexing and Slicing
variable1 = "Ram is a developer"

print(variable1[9:])
print(variable1[0::2])

# Todo: print the variable in reverse

print(variable1[::-1])

# Lists
list_Var = ["a","b","c","d","e"]

list_Var[0] = "Apple"
print(list_Var)

# tuple

tuple_var = ("a","b","c","d","e")

# tuple_var[1] = "apple" #cannot be changed

print(tuple_var[1])

# Todo: change the data in above tuple and printed output should also be tuple


# Todo: remove the duplicate data from the given list

z = ["apple","mango","mango","watermelon","orange"]

z = {"apple","mango","mango","watermelon","orange"}

print(z)

# Dictionaries

a = {
    "name":"niraj",
    "age":"23",
    "hobbies":["TableTennis","Futsal"]
}

print(a["name"])
print(a["age"])
print(a["hobbies"][0][0:5])
