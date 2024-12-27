
# string
a = "hello"
# b = a.upper()

print(a.count("l"))
print(a.upper())

# Lists

new_list = [1,2,3,4,5]
new_list.append(2)
print(new_list)

# tuple

new_tuple = (1,2,3,4,5)
print(new_tuple.count(1))

# Sets

set_a = {1,2,3,4,5}
set_b = {4,5,6,7}
# set_c = set_a.difference(set_b)
# set_a.difference_update(set_b) #changes the value and updates it i.e changes value of set_a
# print(set_a)

set_d = set_a.intersection(set_b)
print(set_d)

set_a.intersection_update(set_b)
print(set_a)

# Dictionaries
bio = {"name":"Ram","age":14}
print(bio.get("name")) #accessing key for the corresponding value
# Get is used in order to stop error as no key it will still return a none
