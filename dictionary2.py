#add values 
x={1:'A' ,2: 'B'}

#y =x[3]# error come because there no key value 3.
#then we can get out value and if not that value we can get anothe value as outpu from "get " key word..
y= x.get(3,0) 
print(y)

#delete value

del x[1]
print(x) 

#to delete all

x.clear()

print(x)