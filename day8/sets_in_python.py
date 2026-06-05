## sets in python 
""" -->> 
    In Python, a set is an unordered, mutable collection of unique elements that does not allow duplicate values. Sets are highly optimized for membership testing (checking if an item exists) and eliminating duplicates from a sequence because they are implemented using hash tables internally.
    
"""
print()

# ----> how to define set data type 
# using the set() function 

numbers = [1,2,3,3,4,5,5,67,77,67,77]
print("data -> ",numbers)
print(type(numbers))
#  lets create set using the list 
numbers = set(numbers)
print()
print("data ->",numbers)
print(type(numbers))
print()

## using the {} 
set_data = {1,22,33,33,22,33,44,55}
print("data -> ",set_data)
print(type(set_data))


## we cannot create blank set using the {} method 
set_blnk = {}
print(type(set_blnk)) ## now the type is dict means dictionary
#  but we can create using the set() method 
set_blnk = set()
print(type(set_blnk))