def my_form(**params): #use two astric to named  parameter..
    if 'name' not  in params:  #when use this coome error 
        print("Error")

    else:    
        print("Hello",params['name'])


my_form(name="Parameete",height=176,city="vavniya")
my_form(height=176,city="vavniya")


#can use both packed argument and named  argument same funtion..
#packed argument should use firstly
