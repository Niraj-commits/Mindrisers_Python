
# Function: Block of code that can be called anywhere inside or outside the program

# Default arguments are the arguments sent inside the parameters

# values sent to the function while function call is called the arguments

def name(nam="Niraj",age= 20): #values used inside function for default values
    print(f"I am a {nam} function")
    print(f"I am {age} Years Old")


firstname = "Niraj"
age = 40

name() #calling the function directly
name(firstname,age) #using global variables to access function
name("Niraj",43) #using arguments to use function

