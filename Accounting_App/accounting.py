
# ask user if they want to register or login
# If register, ask user for name and password and store it in a file permanently
# If login, ask username and password and check if it exist in the file
# if it does print login success if not print invalid credentials
# json.dump converts dictionary to json format
# json.load converts json back to dictionary format

# Todo: Create a dictionary that stores user data like username and password and another one which stores
#  the username and amount ask user for credentials and check if user is valid then show them three options
#  1, check balance 2, withdraw balance and add balance and if the option is check, print the amount of user if option
#  is add ask the user to add in the account and add it with the current balance and lastly if the option is withdraw
#  ask the user for amount and subtract the amount from values and if the withdrawn amount is greater than their balance
#  show them insufficient balance.
import json

def check(username):
    load_acc_detail = open("account_data.txt","r")
    data_in_list = load_acc_detail.read().split(",")
    balance = 0
    for i in data_in_list :
        if i != "":
            dict_data = json.loads(i)
            value = int(dict_data[username])
            balance += value
    print(f"Hi {username}, your current balance is {balance}")

def deposit(username):
    deposit_amount = int(input("How much do you want to deposit?: "))
    for_deposit = open("account_data.txt","a")
    dict_deposit_amount = {username:deposit_amount}
    json_amount = json.dumps(dict_deposit_amount)
    for_deposit.write(json_amount+",")
    for_deposit.close()
    print(f"{dict_deposit_amount[username]} deposited successfully!!")


def withdraw(username):
    account_detail = open("account_data.txt","r")
    prev_entries = account_detail.read().split(",")
    account_detail.close()
    final_balance = 0
    for i in prev_entries:
        if i != "":
            prev_json_data = json.loads(i)
            entry_values = int(prev_json_data[username])
            final_balance += entry_values

    amount = int(input("How much do you want to withdraw?? : "))
    if final_balance > amount:
        withdraw_data = open("account_data.txt","a")
        dict_data = {username:-amount}
        json_data = json.dumps(dict_data)
        withdraw_data.write(json_data+",")
        withdraw_data.close()

        final_balance -= amount
        print(f"Hi {username} your balance is rs.{final_balance}")
    else:
        print("Insufficient Balance")

def login():
    global IsLoggedIn
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    load_data = open("user_data.txt","r")
    list_data = load_data.read().split(",")

    for data in list_data:
        if data != "":
            json_load = json.loads(data)
            if username in json_load and json_load[username] == password:
                print(f"Hi {username}")
                IsLoggedIn = True

    else:
        print("Wrong Credentials")

    if IsLoggedIn:
        account_info = int(input('''What do you wish to do?
1. Check Account
2. Deposit
3. Withdraw
(1 or 2 or 3)--> '''))
        if account_info == 1:
            check(username)
        elif account_info == 2:
            deposit(username)
        elif account_info == 3:
            withdraw(username)

def register():
    username = input("Enter new username: ")
    password = input("Enter your password: ")
    user_info = {username:password}
    user_info_json = json.dumps(user_info)
    store_data = open("user_data.txt","a")
    store_data.write(user_info_json+",")
    store_data.close()
    print("Registration Successful!!!")

user_auth_option = input("Register or Login?? : ").lower()
IsLoggedIn = False
if user_auth_option == "login":
    login()

elif user_auth_option == "register":
    register()

else:
    print("Please Choose Login or Register")