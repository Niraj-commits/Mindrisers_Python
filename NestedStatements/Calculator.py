
while True:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    operator = input("Enter Operator(-+/*): ")
    if operator == "+":
        result =  num1+num2
        print(result)

    elif operator == "-":
        result = num1-num2
        print(result)

    elif operator == "/":
        result = num1/num2
        print(result)

    elif operator == "*":
        result = num1 * num2
        print(result)

    else:
        print("Enter Valid Operator")
        break

    continue_calc = input("Do You Want to continue?: ")
    if continue_calc == "No":
        break
