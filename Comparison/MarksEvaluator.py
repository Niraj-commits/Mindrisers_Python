
# Todo: Get Exam marks as data from user if the marks is greater than 90 and smaller than 100 print excellent

marks = int(input("Enter Your Obtained Marks: "))

if marks >= 90:
    print("Excellent")

elif marks < 40 :
    print("You Fail")

elif marks > 40 and marks<50:
    print("Passed")

elif marks >50 and marks<60:
    print("Could Have Been Better")

elif marks > 60 and marks<70:
    print("Better")

elif marks > 70 and marks<80:
    print("Good")
elif marks>80 and marks<90:
    print("Very Good")