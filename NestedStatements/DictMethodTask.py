# Todo: Store Name as Key and password as value ask user for their name and password if user input exist in dictionary then print login success if not print try again
users = {
    "Ram":"123456",
    "Shyam":"abcdef",
    "Rita":"briefcase"
}
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
for user in users:
    saved_password = users.get(user)
    if username == user and password == saved_password:
        print("Login success")
        break #if no break is used then else will execute
else:
    print("Wrong Credentials") #For Else used in order to return if no value is present
