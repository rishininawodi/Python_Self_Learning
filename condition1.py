# 0-35 w
#35-55 c
#55-65 b
#75-100 a
 # not succes long 
marks = 55

if marks >= 0 and marks<35:
    print("w")

else:
    if marks >= 35 and marks <55:
        print("s")
    else:
        if marks >= 55 and marks<65:
            print("c")
        else:
            if marks >=65 and marks <75:
                print("B")
            else:
                if marks >= 75 and marks <= 100:
                    print("a")
                else:
                    print ("Invalid")


# succes method
marks1 =55
if marks1 >= 0 and marks1 <35:
    print("W")
elif marks1>=35 and marks1 <55:
    print("S") 
elif marks1>=55 and marks1 <65:
    print("C") 
elif marks1>=65 and marks1 <75:
    print("B")                
elif marks1>=75 and marks1 <100:
    print("A")                                         
else:
    print("invalid")


# succes method 2
marks2 =55
if marks2 <0 or marks2 > 100:
    print("Invalid")
    #exit()
elif marks2 >= 0 and marks1 <35:
    print("W")
elif marks2 <55:
    print("S") 
elif marks2 <65:
    print("C") 
elif marks2 <75:
    print("B")                
elif marks2 <100:
    print("A")                                         
else:
    print("invalid")    