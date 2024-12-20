
while True:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    operand = input("Enter Operand(-+/*): ")
    if operand == "+":
        result =  num1+num2
        print(result)

    elif operand == "-":
        result = num1-num2
        print(result)

    elif operand == "/":
        result = num1/num2
        print(result)

    elif operand == "*":
        result = num1 * num2
        print(result)

    else:
        print("Enter Valid Operand")
        break

    continue_calc = input("Do You Want to continue?: ")
    if continue_calc == "No":
        break
