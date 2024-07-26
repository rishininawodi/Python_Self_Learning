def get_grade(*marks):
    total =0
    for i in marks:
        total += i

    print(total)

m= [78,75,43]

get_grade(m) #ok 

#but need pass few arguments like foollow:
#get_grade(78,75,43) give type error..because pass three arguments but define only one parameteer..
# use "packed". define by using star mark front of variable define.

get_grade(78,75,43)

