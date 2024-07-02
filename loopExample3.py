x= [12,34,56,23,45]

count =0
total= 0

while count <len(x):
    item = x[count]
    total +=item
    
    count +=1

print(total)
print(total/len(x))    
