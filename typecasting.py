
# Integer to float datatype
var1 = 10
print(type(var1))

var2 = float(var1)
print(type(var2))

# Float to integer datatype

num1 = 10.1
print(type(num1))

num2 = int(num1)
print(type(num2))

# String to integer

# str1 = "Hi" #cannot be converted because it doesn't have any numerical value
# print(type(str1))
#
# str2 = int(str1)
# print(type(str2))

num3 = float(num1)
print(type(num3))

list_var = [(1,2),("3","4")] #for dictionary it should be in a group of key-value pair

tuple_var = tuple(list_var)
print(tuple_var)

list_var = list(tuple_var)
print(list_var)

set_var = set(list_var)
print(set_var)

dictionary_var = dict(list_var)
print(dictionary_var)