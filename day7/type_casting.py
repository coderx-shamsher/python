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
# type convertion using the int()
alstring = int(alstring)

print()
print(10+alstring)

## string to int 
num1 = "100"
num2 = 20

# now mere pass ek alphanumeric string hai or ek int number or muje use sum krna hai 
# print(num1+num2)
# can only concatenate str (not "int") to str

# how to do calculation without changing the value type , just use type casting 
print(int(num1)+num2) # int function meri alpha numeric string ko int mein convert kr dega..

# also checkout the type of the converted string 
print(num1,"type of alpha numeric string =>", type(num1))
print(num1,"type converted ==> ",type(int(num1)))

# int value into string 
num1 = 10023
print(num1,"type is => ",type(num1))

## using the str function 
print(num1,"type converted =>",type(str(num1)))