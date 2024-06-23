x= [1,2,3,4,5,6]
b=[0,6,34,23,67,89]

y = x[0]
z = x[4]  #getting 4th index
   #a = x[10] #10 th index no in this list.there fore give error

print(y,z)
#print (a)

#add new data to list positions

x[0] = 100
x.append(900)  #add new data to last 
x.insert(2,300) #add new data to middle of list
x.remove(3)  #with data 

print("with remove keyword ",x)

x.pop(1)  #with index


print("with pop :" ,x)

g=x+b
print(g)

#In operator
s =  300 in x

h = not 300 in x
i = 300  not in x

print(s,h,i)

