# Todo: Create a dictionary that stores user data like username and password and another one which stores the username and amount ask user for credentials and check if user is valid then show them three options 1, check balance 2, withdraw balance and add balance and if the option is check, print the amount of user if option is add ask the user to add in the account and add it with the current balance and lastly if the option is withdraw ask the user for amount and subtract the amount from values and if the withdrawn amount is greater than their balance show them insufficient balance.


users = {
    "ram":"iamram",
    "shyam":"iamshyam",
}

account = {
    "ram":45000,
    "shyam":50000,
}

username = input("Enter Your Username: ")
password = input("Enter Your Password: ")

if username in users and password == users[username]: #users[username] here is dictionary[key]
    print(f"Hello {username} welcome")
    response = input("What Do you want to do??(Check,Deposit,Withdraw): ")

    if response == "Check":
        print(f"Your Total is : {account[username]}") #account[username] here is dictionary[key]

    elif response == "Deposit":
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        account[username] += deposit_amount
        print(f"Your total is now {account[username]}")

    elif response == "Withdraw":
        withdraw_amount = int(input("Enter the amount you want to withdraw: "))
        if withdraw_amount < account[username]:
            account[username] -= withdraw_amount
        else:
            print("Insufficient Balance!!!")

    else:
        print("Wrong Value entered")
else:
    print("Sorry!! User not found or Used Wrong Credentials")