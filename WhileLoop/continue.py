
# Continue is opposite of break after use the remaining is not read

# a = 1
# b = 3
#
# while a <b:
#     print("a is smaller")
#     continue
#     a +=+ 1
# continues until infinite loop

a = 0
b = 5

while a <b:
    a += 1
    if a == 4:
        continue #when a == 4 the code below is not executed but redirected to while loop
    print(a)
