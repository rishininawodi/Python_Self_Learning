x={'100':"moneragala" ,'200':"colombo"}#keys are denoted by singlr qutation.value is double quatation
x['1200'] = "galle" # ADD new item to dict

print(x)
print(x.keys()) # to print all keys in dictionary
print(x.values())#to print all values in dictionary

#in dictionary havent data in order.therefore we cant get data from dictionary by index value...
#y =x[0] 
#print(y)

#but if have key value zero it can get 0 key value...
x[0] = "zero"
y =x[0] 
print(y)
print(x)

#key type can change

#one key can add another list
x['cities'] = ['matara' ,'rathnamapur']
z= x['cities']
print(z)

#in dictionary you can put same key type value.but if not same not giving errorr



