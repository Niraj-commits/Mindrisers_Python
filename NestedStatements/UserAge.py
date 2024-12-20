
# Todo: If user age is greater than 18 they are eligible for license
#  if true ask which license they want to take

age = int(input("What is your age: "))
licence_lists = ["Bike","Scooter","Car"]

if age > 18:
    print("Available Options are Bike,Scooter,Car")
    licence = input("What do you need licence for: ")
    if licence in licence_lists:
        print(f"You are eligible for {licence}!!")
    else:
        print("Not Available")
else:
    print("Sorry Try again next time")
