Number_Major = []
for x in range(1,23):
    Number_Major.append(str(x) + "." + (str (input(str(x) + "."))))
    pass
while True:
    p= int(input("Enter Number: "))
    if p < len(Number_Major):
        print(Number_Major[p - 1])
    else:
        print("Error Please try Again!!!")
        pass