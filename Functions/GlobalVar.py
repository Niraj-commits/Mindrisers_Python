
# Global variable when changed inside the function needs to be defined using global keyword inside the function

a = 10

def var_define():
    global a #without this it will not find "a" and if the variable is already inside function it will prioritize local vars
    a = a+10
    print(a)

var_define()