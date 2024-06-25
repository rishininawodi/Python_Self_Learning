#add complex data types to dictionary

x= {
    "a": ['hello' , 'hi' , 'gooy n'],
    "b" :['bye','gn']
}
print(x)

y= x['a']  #put only address of list

y.append('auybown')
print(y)
print(x)#this also have append item becuse y mean x copy.all changes come to x also