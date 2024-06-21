#Call strin  variable

name="Rishini"
print(name)

#operators using
a=10
b=2
c=a+b

print(c)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b) #round value give as output
print(a**b)

#string can only apply + operator
a="Rishini"
b="Nawodi"

c= a+ " " + b

print(a+b)
print(c)
print(a*5)

#string can only concat string.cant concat integer value.it can do following
a="Rishini"
b="Nawodi"
c= 5

d= a + " " + b + str(c) #int convert to string

print(d)

#using boolean 
age= 23
a= True
b=False

is_Young = age<18

is_Equal = age==18 #check whether two values are equal
is_Equal1 = age=18 #assign
c=a and b
d=a or b
e=  not  b
f= a^b #xor =eqaul nm both false.different nm true

print(is_Young)
print(is_Equal)
print(is_Equal1)
print(c)
print(d)
print(e)
print(f)

#operators 
num= 10

print(type(num)) 
print(num,type(num))
num +=5
print(num)

#variable assign single line
num1,num2 = 10,20

print(num1,num2)
