
# Todo: Take two numerical inputs from user and a operator from the user

num1 = int(input("Enter Your first number: "))
num2 = int(input("Enter Your second number: "))
operator = input("Enter Your Operator(+,*,/,-) : ")
result = ""

if operator == "+":
    result = num1+num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "/":
    result = num1/num2
    print(result)

elif operator == "*":
    result = num1*num2
    print(result)

else:
    print("Enter a valid operator")
