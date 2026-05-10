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


