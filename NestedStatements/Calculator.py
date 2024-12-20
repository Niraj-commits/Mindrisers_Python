
while True:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    operator = input("Enter Operator(-+/*): ")
    if operator == "+":
        result =  num1+num2

    elif operator == "-":
        result = num1-num2

    elif operator == "/":
        if num2 != 0:
            result = num1/num2
        else:
            print("Division By Zero\n")
            continue

    elif operator == "*":
        result = num1 * num2
    else:
        print("Enter Valid Operator\n")
        continue
    print(result)
    continue_calc = input("Do You Want to continue?: ")
    if continue_calc == "No":
        break
