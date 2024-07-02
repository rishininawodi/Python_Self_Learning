x= [12,34,56,23,45]

max = x[0]#max =0  
min = x[0]

for i in x:
    if max<i:
        max = i
    if min > i:
        min = i    

print(max)   
print(min)     
