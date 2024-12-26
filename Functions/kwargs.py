
# Kwargs - keyword arguments that returns a dictionary data type , defined using **

def student1(**kwargs):
    print(kwargs)

student1(Name="Ram",Age=43)


# *args can also be used to send some data in *args and other in other as

# def data1(age,*args): #by sending the data before *args
#     print(age)
#
# data1(24,"Ram","Hari")
#
# def data1(*args,age):
#     print(age)
#
# data1("Ram","Hari",age=23)

# You can also use *args and **kwargs at the same time

def data2(age,*args,**kwargs):
    print(age)
    print(args)
    print(kwargs)

data2(20,"Ram","Hari",Name="Ram",Location="KTM")