
# Kwargs are used in order to pass multiple data and make the program dynamic it is used as * before argumentsas
# Data are stored in tuple in kwargs
def student(*args):
    for i in args:
        print(i)

student("hari","shyam","Geeta","Rita") #with *args you can add multiple data