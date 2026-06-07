# ---->>> String Slicing in details ---->>>> 
""" 
    -->>  string slicing method is used to access a range of string characters in the string.
          slicing in a string is done by using the string slicing operator is colon (:). 
          
    Note -- string returned after the slicing includes the character at the start index but not the character at the last index. we will see with example.. 

"""


test = "testing1234"
print()
print("string value ==> ",test,"\n","length of the string ==> ", len(test))
print()



# --- slicing to access all the elements from the string data type 
print("get all string elements --> ")
all_elements = test[0:]  

# what is the meanning of this [0:] ? iska matlab hai k start kro from 0 or : means sare he elements get kro or print kro
print(all_elements)
print()
# same method without 0 
without_0 = test[:] 
# python automatically fill the 0 before the : its like [0:] 
print("same method without 0 in slicing --> ")
print(without_0)

## ager muje sirf testing he chaahie to how to do that with slicing 
print()

slice1 = test[0:7]
print("slicing text from alpha_Numeric string ---> ", all_elements)
print(slice1)

# yeh krne se phale apko indexing ki knowledge honi chaahie..
""" how its work ? 
    
    index samjte hain.. ! 
    
    meri value ki len hai 11 or indexing 0 say suru hoti hai to meri last value 10 index pr honi chaahiye.. jo ki hai bhi.. 
     
     print(test[10]) # hamne test kr k dekh liya..
     
     now muje last k 4 characters nhi chaahie muje sirf string value chaahie main number values koi separate krna chahta hun ? how to do that.. 
     
     or abh slicing start value jo ki 0th index say suru hogi then the slicing operator or than last value abh last slicing kis index tak hogi vo index number pass krna hai... or muje last k 4 numbers nhhi chaahie 10 - 4 = 6 , start from 0,1,2,3,4,5,6
     
     lets break down with code example --->   
"""
print()
print(test[0],test[1],test[2],test[3],test[4],test[5],test[6])
# now it means k muje last 6th index tak ki value he chaahie using the slicing...
# but the rule of slicing is k last ki index value include nhi hoti kiya matlab  hai ? 
# lets do slicing 
print()
print("slicing with extact indexing number")
print(test[0:6])  ## starting from 0 and hamari values last 6th index tak hai !! 
print()
# how to fix this problem ? 
print(test[0:7]) # increase the last index number, ager value 5 par hai to slicing mein 6 put kro as last value !!! 

# hamm ek specific range of string mein say koi bhi charater and word etc get kr sakte hain

# ager kisi string ki between value chaahie to ?? 
test1 = "string_python_slicing"

# mow i need python 

# first find the length 
print(len(test1))

# now ager muje kisi character ka index number nhi pta ho to kiya kre keok string bhot long hai to use find method / function 
index = test1.find("_")

print(test1.find("n_"))
print(test1[12]) 

# now meri checking puri hoyi or now mai slice kr sakte hun
print("my between value =>",test1[7:13])

# this method of finding between values might be hard or not time efficient , but kabhi kabhi jarurrat ho to use krna its okkyy

## find() + slicing method, another way 
text1 = "My name is friday and i live in USA"

start = text1.find("friday")
print(start)
print(text1[11])

end = start + len("friday")

print(end)
print(text1[16])
print(text1[17])

print("final == slicing output..-->")
print(text1[start:end])

## split() method 
words = text1.split()
print() 
print(words)

## yeh ek list of string return krega split function or list k elements ko bhi ham indexing ki help say get kr sakte hain or ese yeh method , say seprate krta hai to ese rehta hai indexing gusse krna easy hai 
print(words[3])

### partition()  method powerfull method 
before,result,after = text1.partition("friday")
print()
print(before)
print(result)
print(after)

## about the partition method --->
#Partition the string into three parts using the given separator.
 #This will search for the separator in the string. If the separator is found,
  #returns a 3-tuple containing the part before the separator, the separator
   #itself, and the part after it."


print()

text101 = "this linux is the most powerfull os in the world"

part1,part2,part3 = text101.partition("most")
print(part1,type(part1))
print(part2,type(part2))
print(part3,type(part3))

### simple way jis value ki slice krna hai use partition method mein pass kro or use ek middle position variable mein store kro or that it its easy to get this value , bs jis value ko splice krna hai vo mid variable mein store hoti hai or baki divide ho jate hain 3 parts mein ... 2 vala part hamara result hota hai... 

# print(part2)
# print(part3)
subpart1  = part1.partition("linux")
print(subpart1,"\n",type(subpart1))

## use indexing to get element from tuple now... 
print(subpart1[0])

# Dynamic extraction
text = "Order ID: 45872 | Status: Success"

start = text.find("Order ID: ") + len("Order ID: ")
end = text.find(" |")

order_id = text[start:end]
print()
print("Order id ---> ")
print(order_id)

#### advanced 
text = "apple mango apple banana"

print(text.find("apple"))     # first occurrence
print(text.rfind("apple"))    # last  occurrence

test11 = "this is python and its very powerfull, python is used for AI/ML Nowdays"
print() 
first = test11.find("p")
last = test11.rfind("p")
print([first])
print([last])

## split() method with keyword 

txt1 = "linux is the king of Os"
result = txt1.split("the ")[1]
print(result)

result = result.split(" of")[0]
print(result)
print()
## this method split() break down 
## jo bhi value split function main pass hoti hai us jagah string cut hoti hai 

test001  = "linux have ubantu arch fedora red-hat debain"

## using he split() method 
### this is step 1 
splited_value = test001.split(" ")
print(splited_value)
print()
splited_value = test001.split("ubantu ")
print(splited_value)

## hamne string ko ek list mein break kr liya... 
## keo k split() method ek list he return krega hamesa to jis value ko pass kroge to us jagah te including your passed string value cut ho jayegi jaise maine "ubantu " pass kiya mean "ubantu " koi include krte hoye meri string break hogi
print()
print(splited_value[0])
print(splited_value[1]) 
print()
## now muje arch chaahie to let do same method 
result2 = splited_value[1].split("fedora")
result2 = splited_value[1].split("fedora")[0]
print("MY sliced value is =>",result2)

# you can do below method to do the same thing..
# print(result2[0])

