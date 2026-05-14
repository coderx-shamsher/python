## type casting is converting variables types from one to another using some functions

# implicit type convertion is method that python used to convert or type cast variables automatically 

# int data type 
var = 110

# how to check type of variables 
# using the type() function we can check the type of any veriable
print("type of ",var,"is => ",type(var))

#  type convertion  explicit type convertion 

# int to float 
var = float(var)
print()
print("type casted ==> ",var," ", type(var))


# into string 
var = str(var)
print(var," type casted ==> ",type(var))

## 
alstring = "100"
print(type(alstring))

# alphanumeric string value into int or float

print(alstring,"type casted ==>",type(int(alstring)),)
alstring = int(alstring)

print()
print(10+alstring)