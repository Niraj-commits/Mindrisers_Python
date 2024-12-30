# Todo: Ask user for name and age and write them in file , name as key and age as value

name = input("Enter Your name: ")
age = int(input("Enter Your age: "))

details = {name:age}
user_info = open("../WriteTask.txt", 'a')
user_info.write(str(details))
user_info.close()
