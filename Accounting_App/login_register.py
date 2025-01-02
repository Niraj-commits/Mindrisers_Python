
# Requirements
# ask user if they want to register or login
# If register, ask user for name and password and store it in a file permanently
# If login, ask username and password and check if it exist in the file
# if it does print login success if not print invalid credentials
# json.dump converts dictionary to json format
# json.load converts json back to dictionary format


import json

def login():
    username = input("Enter Your username: ")
    password = input("Enter Your Password: ")

    retrieved_data = open("user_data.txt", "r")
    read_data = retrieved_data.read().split(",") #split(",") to know where to split the data
    print(read_data) #returns all the data in list form separated by split(",")
    for i in read_data:
        if i !="":
            dict_data = json.loads(i) #doing inside if because the last value is " " which will cause problem
            print(dict_data)
            if username in dict_data and dict_data[username] == password :
                print(f"Login Successful! Hello {username}")
                break
    else:
        print("Wrong Credentials")
    retrieved_data.close()



def register():
    username = input("Enter Your Username: ")
    password = input("Enter New Password: ")

    stored_data = {username:password}
    json_data = json.dumps(stored_data) #converting dictionary to JSON format
    user_info = open("user_data.txt", "a")
    user_info.write(json_data+",") #while sending data we added "," so it can be split easily
    user_info.close()
    print("Registration Completed!!!")

choice = input("Do you Want to Login or Register: ")

if choice == "login":
    login()

elif choice == "register":
    register()

else:
    print("Please Choose Login or register")