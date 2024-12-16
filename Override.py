#
#
# var1 = "Hello"
# var1 = "World" #overrides the value of variable "var1"
# print(var1)
# print(var1[0])
# print(var1[0:3])
#
# # Indexing and Slicing
# variable1 = "Ram is a developer"
#
# print(variable1[9:])
# print(variable1[0::2])
#
# Todo: print the variable in reverse
variable1 = "Ram is a developer"
print(variable1[::-1])
#
# # Lists
# list_Var = ["a","b","c","d","e"]
#
# list_Var[0] = "Apple"
# print(list_Var)



# Todo: change the data in above tuple and printed output should also be tuple

tuple_var = ("a","b","c","d","e")

# tuple_var[1] = "apple" #cannot be changed
print(tuple_var)

list_var = list(tuple_var)

list_var[0] = "apple"

tuple_var = tuple(list_var)

print(tuple_var)

# Todo: remove the duplicate data from the given list

z_list = ["apple","mango","mango","watermelon","orange"]

z_set = set(z_list)

z_list = list(z_set)

print(z_list)

# Dictionaries

# a = {
#     "name":"niraj",
#     "age":"23",
#     "hobbies":["TableTennis","Futsal"]
# }
#
# print(a["name"])
# print(a["age"])
# print(a["hobbies"][0][0:5])
