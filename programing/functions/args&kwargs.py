# *args and **kwargs are used in Python functions to allow for variable numbers of arguments.

#--------------------------------------------------------------
def sumof(*args):
    return sum(args)
print(sumof(1, 2, 3, 4, 5))

# --------------------------------------------------------------
def intro(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
intro(name="John", age=30, city="New York")

# local variable
def local_variable():
    x = 10
    print(f"Local variable x: {x}") 

#--------------------------------------------------------------
# global variable
y = 20  
def global_variable():
    global y
    y += 5
    print(f"Global variable y: {y}")
#--------------------------------------------------------------

def main():
    x = 10
    global y
    # y = 20
    print(f"Inside main - Local variable x: {x}, Global variable y: {y}")
#---------------------------------------------------------------
main()
local_variable()
global_variable()
