x= [12,34,56,23,45]
count =0
total = 0


max = x[0]#max =0  
min = x[0]

while count <len(x) :
    item = x[count]

    if item >max :
        max = item
    if item<min:
        min=item

    count += 1        


print(max)   
print(min)     
