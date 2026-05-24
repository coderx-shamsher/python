#In Python programming, Operators in general are used to perform operations on values and variables.
#Operators: Special symbols like -, + , * , /, etc.
#Operands: Value on which the operator is applied.


'''
1) Arithmetic Operators 
Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.

'''


#  addition ( + ) 

a = 200 
b =  300 
print(a,"+",b,"is =",a+b)

# subtraction ( - )
print(b,"-",a,"is =",b-a)

# multiplication ( * )
print(a,"*",b,"is =",a*b)

# Division ( / )
num1 = 240
num2 = 8
print(num1,"/",num2,"is =",num1/num2)


# floor Division ( // )
print(num1,"//",num2,"is =",num1//num2)

" -> Note -> In Python, the division operator (/) returns a floating-point result, while floor division (//) returns an integer result. "


# modulus ( % )
print(num1,"%",num2,"is =",num1%num2)

# exponentiation ( ** )
n1 = 2
n2 = 4 
print(n1,"**",n2,"is = ", n1**n2)
# 2 * 2 * 2 * 2   2 ** 4 means 2 ko 4 bari multiple kro kaise ? -> 2 * 2 = 4 * 2 = 8 * 2 = 16
# that's how exponentiation works 
  
print()
print(n1*n2)
print(2**3)

print()
"2) Comparison Operators -> Comparison(or Relational) operators compares values. It either returns True or False according to the condition."

# == equal to opr 
var1 = 20
var2 = 22
print(var1,"==",var2," ->",var1 == var2)
print()

# != not equal to 
print(var1,"!=",var2," ->",var1 != var2)
print() 

# > greater then 
print(var1,">",var2," ->",var1 > var2)
# print(var1 > var2)
print()

# < less then 
print(var1,"<",var2," ->",var1 < var2)
# print(var1 < var2) 
print()

# >= greater than equal to  yeh dono conditions ko check kreha > and = to 
print(var1,">=",var2," ->",var1 >= var2)
# print(var1 >= var2)
print()

# <= less than equal to 
print(var1,"<=",var2," ->",var1 <= var2)
# print(var1 <= var2) 
print()

# Assignment OPR
"Assignment operators are used to assign values to the variables. This operator is used to assign the value of the right side of the expression to the left side operand. Example:"

# = assignment opr
a = 200
print("this is the assignment opr ")
print()

# Assignment operators with arithmetic assignments 

# 1) a = a + value/number/variable
a = 369 
b = 1 

# variable 
print("before Assignment => ",a)
a = a + b 
print("After Assignment => ",a)

print()
# 2) a += value/number/variable
print("before -> ",a,"\n")
a += b 
print("after -> ",a)


"or ham same he subraction, or other arithmetic operators use kr skate hain. example -> alll he bitwise oprs etc... "


# ---> enforce  precedence with parentheses 
print()

numX= 1+3*2   # how this calculations is done lets see the answer first 
print(numX)   # 7 but how 7  calculation to kuch ese honi chaahie 1+3 = 4 *2 = 8 but python mein esa nhi hota.. first  3*2 = 6 + 1 = 7 

# first multiplication then Plus 

# let's see another  example with parentheses 
numY = (2 + 2) * 2
print()
print(numY)

# here we add parentheses or es k sath he calculation ki priority change hogi  first without parentheses 1) multiplication then plus but now hamne plus ko parentheses mein rahkha hai or multiplication parentheses k bahar hain 

# with parentheses 
# first plus or whatever the operator you give in parentheses 
numV = (20 - 10 ) * 2 
print()
print(numV)

### ------>>>>> these are the calculation priorities in python with operators and parentheses 



### -------> logical operators  <-------- ### 
## 1) and 2) or 3) not  


# ----->  here is the not  operator with boolean values 
print("first how the normal boolean values ")
print("true value ==> ", True)
print("false value ==> ", False)
print()


print("not with false ==> ", not False)
print("not with true ==> ", not True)

# how not works if you give false value to not , to yeh us value ko true mein change krdega or true ko false mein 

print()
## and logical operator with 
print("and with boolean ==> ", True and True )
print("and with boolean ==> ", True and False )
print()
# how and logical operator works
# ager dono conditions ka output true hoga to true milega....
print()

## or logical operator 
print("or with boolean ==> ", True or False)
print("or with boolean ==> ", False or False)

##  how or works 
## ager dono conditions mein say koi ek  bhi true hain to output true milega.. ager dono he false hai to false.. 









