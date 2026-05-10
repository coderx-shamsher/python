#          // day one in python \\ 

# 1. print statement / print function(method)
# print() is a built-in function in Python that is used to display output on the console. It can take multiple arguments and will print them to the console, separated by a space by default.
print()
print("this is first day in python " )

# => how to print of run the python code just open the terminal and type the python and then 
# python filename.py 

# ham print() function mein multiple values ko print kar sakte hain, aur ham unko comma se separate krte hain  
print("String values => ")
print("this is hello","python")
print()

print("Numbers/Integer values => ", 234,369,963)
print()
print("Float values => ", 3.14, 2.718, 1.618)
print()
# what is that integer and float values we will disuss in the next topic name Data types in python .

# 1) print () mein ham es trah say print kr sakte hain values koi or now ham dekhenge concept of the variables in python 

"Multiple Assignments"
# Assigning Same Value: allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value. 

num1 = num2 = num3 = 100 
print("multiple assignments :- assigning same values to more then one variable")
print(num1)
print(num2)
print(num3)
print()

# Assigning different values using same method 
n1 , n2 , n3 = "hello","linux","its me"
print(n1)
print(n2)
print(n3)

x = 1 
print()
print(x)
y = x 
print(y)
x += 2
print(x)
print()
y += 2 
print(y)

"""
   # Explanation:

 # Initially, both x and y reference the same object 1
    # When y = y + 1 is executed, python creates a new object 2
      # y now references this new object and x still references the original object 1
        # So, changing y does NOT affect x


"""


