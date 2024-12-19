
# when there is if statement inside another if then it is called a nested if statement

# todo: get two inputs from users (s,p,r) and

user1 = input("Enter Your Selection User1: ")
user2 = input("Enter Your Selection User2: ")

if user1 == "s":
    if user2 == "p":
        print("user1 won")
    elif user2 == "s":
        print("It is a draw")
    elif user2 == "r":
        print("user2 won")

elif user1 == "p":
    if user2 == "r":
        print("user1 won")
    elif user2 == "s":
        print("user2 won")
    elif user2 == "p":
        print("It is a draw")

elif user1 == "r":
    if user2 == "r":
        print("It is a draw")
    elif user2 == "s":
        print("user1 won")
    elif user2 == "p":
        print("user2 won")

else:
    print("Invalid Input")