midterm = int(input("คะเเนนกลางภาค = "))
final = int(input("คะเเนนปลายภาค = "))
sore = int(input("คะเเนนเก็บ = "))
pernal  = int(input("จิตพิสัย = "))
All = midterm+final+sore+pernal
#print("all_score" , All)

if midterm <=30 and final <=30 and sore <=30 and pernal <=10:
    if All <= 100 and All >= 80:
        G = "4"
    elif All >=70:
        G = "3"
    elif All >= 60:
        G = "2"
    elif All >= 50:
        G = "1"
    elif All <= 50:
        G = "0"
    pass
    print("grade" , G)
    pass
else:
    print("(error)กรุณากรอกคะเเนนใหม่")
    

             
