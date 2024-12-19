# while loop is a multiline and conditional statement
# Works when the condition true until it is stopped

a = 5
b = 0

while b < a:
    print("b is Less than a")
    b += 1 #for stopping infinite loops
    print(f"New value of b is now {b}")