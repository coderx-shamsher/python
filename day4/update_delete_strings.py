###  ----> updation/deletion of element of string <------
"strings mein elements/characters ko update/delete krna allowed nhi hai in python, because string is immuatable  "
### let do this task , ager python yeh krna allowed nhi krti hai to kaise hoga... 

## 1 way convert string into list 

__str = "1234_string"

## convertion 
__str = list(__str)
print(__str,type(__str))

## now do the list elements updation 
 ## mai meri 6th index ki value ko update krunga 
print(__str[0]) 

__str[0] = "b1010"
print(__str)

print()
## use .join() to join the string , esa krte he list ka type str mein converted hojayega.... 
__updated = "".join(__str)
print(__updated,type(__updated))
print()

"""  ________work flow of list convertion method to update string value_______


               string value 
                    | 
                    |
                    |
              list convertion 
                    |
                    |
                    |
               Modify list 
                   |
                   |
                   |
    join the list(string) using the .join method          
                  |
                  |
                  |  
              now we have new string (updated string)    
                  
"""
##  method 2 slicing 
__str1 = "vancouver" 
__update = "V" + __str1[1:]
print(__update)
print()


## 3 method replace () method 
__text = "Hello ! linux"

## replace method 
updated = __text.replace("linux","Arch Linux")
## replace method koi old value than new value pass krni hoti hai 
print(updated)
print()
## delete using the slicing 
text_001 = "python00"
print(text_001)
delete = text_001[0:-2]
print("Deleted string ==> ",delete)
print()

print(text_001[:2])

print(text_001[3:])

print(text_001[:2]+text_001[3:])

# use del keyword to delete entire string 
del text_001
print(text_001)