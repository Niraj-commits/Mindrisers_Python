
# Todo
# Requirements
# ask user if they want to register or login
# If register, ask user for name and password and store it in a file permanently
# If login, ask username and password and check if it exist in the file
# if it does print login success if not print invalid credentials
# json.dump converts dictionary to json format
# json.load converts json back to dictionary format


import json

def login():
    username = input("tell me your username chief: ")
    password = input("insert THE code: ")

    retrieved_data = open("user_data.txt","r")
    retrieved_data.close()



def register():
    username = input("Hi, Chief what should I call you? :")
    password = input("insert your code: ")

    stored_data = {username:password}
    json_data = json.dumps(stored_data)
    user_info = open("user_data.txt","a")
    user_info.write(str(json_data))
    user_info.close()


