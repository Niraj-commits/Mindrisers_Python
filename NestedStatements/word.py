
# Todo: Ask user to ask user for the word to keep in loop
#  ask user for the amount of times to run the loop
# print the word for that amount of times

word = input("Enter Your word: ")
loop_times = int(input("Enter the number of times to run: "))

while loop_times >0:
    print(word)
    loop_times -= 1