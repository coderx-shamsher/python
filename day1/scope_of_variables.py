### variable scopes 

""" 
    Local scope variables : - local variables in python are the onces that are defined and declared inside a function, we can not call this variable  outside the function 
       
"""

## lets see a basic function syntax in python 

def local_function():
       print("this is a function ")
       print()
       local = "x is past"   
       print("local variable -----> in local scope ") 
       print(local)   

## this is how to create a function using def keyword in python with : then indentation 
# calling / invoking a function 
# call a function using function name

local_function()

# what is the point ? the point is we cannot use local scope variables outside the scope because its locally assigned lets say... 
# print(local)

print()
gb = "dont waste time on wrong persons"
def random():
    print("this is global scope testing function ")
    # print(gb)
    
    # 
    # gb = "100S009"
    print()
    # print(gb) we cannot change  the value of the gloal variable 
    
    # lets use global keyword 
    global gb 
    gb = "updated value"
    print(gb)
    
    # we cannot update global variable in local
    
     
# calling function 
# random()



# using global keyword , creating global variable 
x = "not now" 

# def fun():
    # print(x)
    # global x
    # print(x) 
    
    
    
# fun()

#  glocal updation
print(gb)
gb = 100
print(gb) 

# we can update global variables in the global scope only 