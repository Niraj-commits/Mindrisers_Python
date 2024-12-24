# Keyword Arguments store data while calling the function in any way as long as you specify while calling with a keyword

def full_name(firstname, lastname,age):
    print(firstname,lastname,age)

fname = "niraj"
lname = "karki"
ages = 23

full_name(lastname=lname,firstname=fname,age=ages)
#can be assigned to any way doesn't matter which comes first


# Local Variables are the variables defined inside the function
#Global Variables are the variables defined outside the function