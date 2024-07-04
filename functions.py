#This method corrrect but not success fully
marks =74

def findgrade():
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
#this method not fully succes
findgrade()
marks=4
findgrade()

#Suuceess method


def findgrade(subject ,marks):
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
#pass value only given order
findgrade("English",66) #pass value and call function

findgrade("Python",56)