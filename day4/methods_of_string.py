#### String methods in detail ... 

## upper() method  --> convert all characters to uppercase 

txt = "This line is string testing in python"

## using f string method to use variables within strings
print(f"Normal string ---> \n {txt}")
print()
print(f"upper method ----> {txt.upper()}")
upper_str = txt.upper()
print() 

## lower method to convert into lower case 
print(f"lower method ---> {upper_str.lower()}")
print()

## to uppercase or capitalize first char only use the caplitalize  method 
print(f"capitalize method --> {txt.capitalize()}")
print()

## now ager har word ka first char upper case krna hai to use title method 
print(f"title method --> {txt.title()}")