from colorama import Fore, Style, init
init()

''' Docstring for datatypes
    today we cover datatypes in python and how to code with them

> what is data type , data type is a classification of data which tells the compiler or interpreter how the programmer intends to use the data. or ham bol sakte hain k data type koi bhi data ka type hota hai means jo data ham variables etc mein use kr rahain hain uska type kiya hai... 

> in python we have several built in data types which are used to store different types of data

'''
# numeric data types
# 1) integer data type

x = 100 
# this is an integer data type because it is a whole number without any decimal point
print()
print("this is an integer data :-", x)
print()
# lets use the f-string to print the variables in the string value, ham f-string ka use karte hain jab hame string ke andar variable ko print karna hota hai, f-string ka use karne ke liye hame string ke starting mein f lagana hota hai aur variable ko curly braces {} ke andar likhna hota hai
print(f"the value of integer variable is => {x} and its type is => {type(x)}")

# 2) float data type 
flt = 10.33 
# this is a float data type because it is a number with a decimal point
# ham ese floating point number or decimal number bhi bol sakte hain
print()
print(Fore.BLUE + f"the value of float variable is => { flt } and its type is => {type(flt)}")

# ham use kr rahe hain colorama module to print the output in different colors, colorama module is a python library which is used to print the output in different colors in the terminal, ham ise install kar sakte hain pip install colorama command se
print()

print(Fore.RED + "This is a red colored output using colorama!" + Style.RESET_ALL)
print()

# 3) complex data type
complexnum = 333+33j
print(f"complex value =>{Fore.YELLOW + str(complexnum) + Style.RESET_ALL} and its type is => {Fore.YELLOW + str(type(complexnum)) + Style.RESET_ALL}")


# string data type
print()
name = "python programming"
print(f"the value of string variable is => {Fore.GREEN + name + Style.RESET_ALL} and its type is => {Fore.GREEN + str(type(name)) + Style.RESET_ALL}")
print()

# Boolean data type 
# es mein values two types ki hoti hai True yan False 
boolval = True 
print()
print(f"the value of boolean variable is => {Fore.LIGHTBLUE_EX + str(boolval) + Style.RESET_ALL} and its type is => {Fore.LIGHTBLUE_EX + str(type(boolval)) + Style.RESET_ALL}")
print()

# now hamne kuch basic data types cover kiye hain or ham age or data types bhi code krenge ... 


