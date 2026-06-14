#### String methods in detail ... 

## upper() method  --> convert all characters to uppercase 

txt = "This line is string testing in python"

## using f string method to use variables within strings
print(f"Normal string ---> \n {txt}")
print()

## ----->> upper () <<------
print(f"upper method ----> {txt.upper()}")
upper_str = txt.upper()
print() 

## ----->> lower() <<----- method to convert into lower case 
print(f"lower method ---> {upper_str.lower()}")
print()

## ----->> capitalize () <<------
## to uppercase or capitalize first char only use the caplitalize  method 
print(f"capitalize method --> {txt.capitalize()}")
print()

### ----->> title <<-------
## now ager har word ka first char upper case krna hai to use title method 
print(f"title method --> {txt.title()}")


## ----->> swapcase() <<-------- method to convert uppercase lower reverse 
print()
print(f" string value --> {txt} ")
print(f"swapcase method --> {txt.swapcase()}")

swapcase_str = "tHIS LINE IS STRING TESTING IN PYTHON"
print(f"--> {swapcase_str.swapcase()}")

# another example 
swap_str = "String Typed ConverT inTo UpperCaSe"
print(f"--> {swap_str}")
print(f" \n -->{swap_str.swapcase()}")
print()


## ---->> count () <<------- method  
print(f"----> {swap_str}")
print(f" count p character in string --> {swap_str.count("p")} ")
# how many p or specific character you want to count from string , yeh method us specific character ki counting return 


## ------->> startwith method <<------ 
print()
print(f'check string with startwith -- {"@shamsher__".startswith("s")}')
print(f'check string with startwith -- {"@shamsher__".startswith("@")}')

##  --->> endwith () <<----- method check if a string ends with specified ending 
email = "codex_python_@gmail.com"
print()
print(f" ---> {email}")
print(email.endswith(".com"))
print(email.endswith("gmail.com"))
#  ager string specific string say end hoti hai to yeh return krta hai boolean value true if matched false if not 


## ---->> expandtabs() <<<----- method replace tab characters with spaces, default tab size is 8 it takes tab size arguments.

txt = "code \tof \t100 \tdays \tin \tpython"

## \t for tab spaces 
print()
print(txt)
print()
print(txt.expandtabs(2),"\n")
print(txt.expandtabs(6),"\n")
print(txt.expandtabs(8),"\n")

print() 

### ----->> find() <<------  returns the index of the first occurrence of a substring, if not found return -1 
text1 = "string methods testing py file py"
print(f" find () p   ----->    {text1.find("p")}")
print(f" find () y  ----->    {text1.find("y")}")
print()

## -------->> rfind() <<------- returns the index of the last occurrence of a substring, if not found returns -1 
print() 
print(f"rfind method p ---> {text1.rfind("p")}")
print(f"rfind method py ---> {text1.rfind("py")}")

## --->>> format() <<<----- formats string into a nicer ouput 
print()
username = "Coderx"
role = "python backend dev"
country = "Vinland"

print("Hi 👋 am {} \n Im doing {}🌐 \n At {}🌄🏕️🏞️ ".format(username,role,country))
print()

## eays and modern way to do this 
### ------>> F string in python  <<---------
print(f"This is the F string {username} and My role => {role} at {country}")


print()
## ----->>> islanum method <<-------
alstring = "this is 1234"
print(f" check alpha num string ---> {alstring.isalnum()}")

##  ----->> isdigit() <<----- method only digit in string ? 
print()
digit_str = "1234"
print(f" is digits in string ===> {digit_str.isdigit()}")
print() 

## ------>> islower method <<----- to check lowercase characters 
testing1 = "shasha is good girl"
print(f'is my string is lower -- {testing1.islower()}')
print(f'is my string is upper -- {"THIS STRING US UPPER".islower()}')
print(f'is my string is upper -- {"THIS STRING US UPPER".isupper}')

## ----->> isalnum <<------
print()
print(f'is this string is alpha numeric ? -- {"12233string".isalnum()}')
print(f'is this string is alpha numeric ? -- {"12233 string ".isalnum()}')

### ----->>> isdecimal() <<----- decimal value 0 - 9 only 
print()
print(f"is this string is decimal ----{'99224'.isdecimal()}")

## ------>>> isspace <<<---- method only spaces? not single character ? 
print(f"is spaces in my string -- {' '.isspace()}")

##  ------->>> index <<------ method 
text2 = "texting python method"
print(f"index method ---> {text2.index("p")}")
print(f"index method ---> {text2.index("o")}")


## ---->> rindex method <<------
print() 
print(f"rindex o --> {text2.rindex("o")}")
print(f"index o --> {text2.index("o")}")


### --------->> strip() <<--------  removes all given characters starting from the begginning and end of the string 
print()
str_with_wrong_char = " v  this string with spaces  This python file is v "
print(f"strip() method --> {str_with_wrong_char}")
print(f"strip() method --> {str_with_wrong_char.strip(' v ')}")
print() 

email = "___sham_23344_33@gmail.com__"
print()
print(f" remove special character --> {email.strip("_")}")

## ---->> replace <<-----  methods 
print() 
testing1 = "python ! code"
print(f" {testing1} \n replaced -- {testing1.replace("python", "hello python")}")
print()


### --------->> join method <<------- method returns a concatenated string 
list_of_string = ['html','css','js','react']
print()
print(f"{list_of_string}\njoin list of string values into on string --- {" ".join(list_of_string)}")
print(f"\njoin list of string values into on string --- {"#  ".join(list_of_string)}")
      
      
## --------->> split method <<----------  split the string using given string or space as a separator 
print()
testing_str = "linux Macos winidows servers"
print(testing_str)
print(f" using split -- {testing_str.split()}")
print()
testing_str = "this, string, methods, are, boring,"
print(f" using split -- {testing_str.split(", ")}")

