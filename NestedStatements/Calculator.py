try:
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
                continue #Continue so that the while loop starts again

        elif operator == "*":
            result = num1 * num2
        else:
            print("Enter Valid Operator\n")
            continue #Continue so that the while loop starts again

        print(f"result = {result}") #Printing Results of any operation at once

        continue_calc = input("Do You Want to continue?: ") #new variable for while to continue or not
        if continue_calc == "No": #for when stopping the while loop
            break

except ZeroDivisionError as err:
    print(err)

except TypeError as err:
    print(err)

except NameError as err:
    print(err)

except ValueError as err:
    print(err)