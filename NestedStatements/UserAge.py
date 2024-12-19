

# Todo: If user age is greater than 18 they are eligible for license if true ask which license they want to take


age = int(input("What is your age: "))
eligible = False

if age > 18:
    eligible = True
    license = input("What do you need license for: ")
    while eligible:
        print(f"You are eligible for {license}")
        break
else:
    print("Sorry Try again next time")