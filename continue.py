x = [1,4,7,8,5,4]

count =0
for i in x:
    if i%2 ==0:
        continue  #skip this itteraton

    print(i)


#while loop
while count == len(x)-1:
    print("index",count)

    j = x[count]

    if j % 2 ==0:
        count+=1
        continue

    print(j**2)

    count +=1
    
