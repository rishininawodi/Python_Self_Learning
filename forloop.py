x= [12,3,4,5,6,7]
index = 0
#print list item
for item in x :
    y = x[index]
    print(index ,y)
    index +=1


x1= [12,3,4,5,6,7]

#print list item
#enumerate function return always tupple with value and index
for item in enumerate(x) : # can use " for index,value in enumerate(x)"
    index =item[0]
    value = item[1]
    print(index,value)


for num in range(0,10):
    print(num)  

r= range(0,10)
print(type(r)) 
r1= range(0,len(x))   
for item in r1:
    print(item) 
   

