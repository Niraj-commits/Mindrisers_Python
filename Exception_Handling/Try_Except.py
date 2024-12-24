
try:
    a = int(input("Enter Your Number: "))
    b = int(input("Enter second number: "))
    print(a/b)

except ValueError as err:
    print(err)

except ZeroDivisionError as err:
    print(err)