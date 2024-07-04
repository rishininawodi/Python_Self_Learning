
def findgrade(marks ,subject="unknown"): 
    print("subject is:" ,subject)
    if marks <0 or marks>100:
      print("Invalid")
    elif marks < 35:
      print("W")
    elif marks < 55:
      print("S")  
    elif marks < 65:
      print("C") 
    elif marks < 75:
      print("B")

    else:
      print("A")  

findgrade(subject="maths",marks=78)     #can pass value using variable name.. 
#findgrade(marks=34, "sinhala")#after name arguments all arguments should name arguments