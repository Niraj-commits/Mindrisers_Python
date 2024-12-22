# Todo: Define a list of users and ask user for their username and check if it is in list or not

username = ["Ram","Sita","Gita"]

for _ in username:
    usernames = input("Enter your username: ")
    if usernames in username:
        print("Login Successful")
        break
    else:
        print("Failed")
        break