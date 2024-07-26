def get_grade(*marks):

    print(type(marks))  #tuple

    total =0
    for i in marks:
        total += i

    print(total)
get_grade(78, 75, 43)





