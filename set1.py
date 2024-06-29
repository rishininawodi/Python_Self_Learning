x={"Hello","World"}

print (x)

x1 = {"Hello","World","Hello"}
print(x1) #same out put.not get dublicate value and no sequenciaal manner

x.add("World")
print(x)

x.add("world")#add to set because simple W 
print(x)

x.remove("World")
print(x)

a={"rishi","nawo","1"}
b={"1","2"}

z= a.union(b)  #add two set method 1
print(z)

z1= a|b#add teow set method 2
print(z1) 

z2 = a-b
print(z2)

print("nawo" in z2 )
print("nawo" not in z2 )
