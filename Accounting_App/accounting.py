
# ask user if they want to register or login
# If register, ask user for name and password and store it in a file permanently
# If login, ask username and password and check if it exist in the file
# if it does print login success if not print invalid credentials
# json.dump converts dictionary to json format
# json.load converts json back to dictionary format

# Todo: Create a dictionary that stores user data like username and password and another one which stores
#  the username and amount ask user for credentials and check if user is valid then show them three options
#  1, check balance 2, withdraw balance and add balance and if the option is check, print the amount of user if option is add ask the user to add in the account and add it with the current balance and lastly if the option is withdraw ask the user for amount and subtract the amount from values and if the withdrawn amount is greater than their balance show them insufficient balance.

import json

def check(username):
    check_account = open("account_data.txt","r")
    check_data = check_account.read().split(",")
    user_balance = 0
    for i in check_data:
        if i != "":
            acc_data_json = json.loads(i)
            if username in acc_data_json:
                user_amount = int(acc_data_json.get(username))
                user_balance += user_amount
    print(f"Your total is {user_balance}")


    check_account.close()

def deposit(username):
    initial_balance = 0
    amount = int(input("Enter the amount you want to add: "))
    add_in_acc = open("account_data.txt","a")
    final_amount = initial_balance+amount
    acc_value = {username:final_amount}
    add_in_json = json.dumps(acc_value)
    add_in_acc.write(add_in_json+",")
    add_in_acc.close()

# def withdraw(username):
#     pass
def login():
    global isLoggedIn
    username = input("Enter Your username: ")
    password = input("Enter Your Password: ")

    retrieved_data = open("user_data.txt","r")
    read_data = retrieved_data.read().split(",") #split(",") to know where to split the data
    print(read_data) #returns all the data in list form separated by split(",")
    for i in read_data:
        if i !="":
            dict_data = json.loads(i) #doing inside if because the last value is " " which will cause problem
            if username in dict_data and dict_data[username] == password :
                print(f"Login Successful! Hello {username}")
                isLoggedIn = True

    if isLoggedIn:
        user_choice = int(input('''
What Do you want to do?
1. Check
2. Deposit
3. Withdraw
--> '''))

        if user_choice == 1:
            check(username)

        elif user_choice == 2:
            deposit(username)

        # elif user_choice == 3:
        #     withdraw(username)

        else:
            print("invalid operation")
    else:
        print("Wrong Credentials")
    retrieved_data.close()



def register():
    username = input("Enter Your Username: ")
    password = input("Enter New Password: ")

    stored_data = {username:password}
    json_data = json.dumps(stored_data) #converting dictionary to JSON format
    user_info = open("user_data.txt","a")
    user_info.write(json_data+",") #while sending data we added "," so it can be split easily
    user_info.close()
    print("Registration Completed!!!")

choice = input("Do you Want to Login or Register: ")
isLoggedIn = False

if choice == "login":
    login()

elif choice == "register":
    register()

else:
    print("Please Choose Login or register")