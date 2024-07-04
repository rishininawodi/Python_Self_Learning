

#if have default value parameter.then also should have othe after all parameters as default
def findgrade(marks ,subject="unknown"): #can subject convert to optional
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


findgrade(30)# there no need subject value because it optional      