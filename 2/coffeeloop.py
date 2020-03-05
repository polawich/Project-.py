member = ""
name = ""
dc = ""
colum = ""
for colum in range(1,11):
    name = str(input("Input your name : "))
    if colum <= 3:
        dc = 50
    elif colum <= 6:
        dc = 30
    else: 
        dc = 15 
    pass 
    member = str(member + str(colum) + "." + "Name : " + str(name) + " (discount) " + str(dc) + "%" + "\n" )
    print(member)
pass

