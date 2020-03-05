from tkinter import*
root = Tk()
root.option_add("*Font","consolas 20")
root.geometry("500x300")

it=IntVar()
mt=IntVar()
mh=IntVar()
eai=IntVar()
result  = StringVar()

Label(root, text = "Student Name = ").grid(row = 0,column = 0 , stick = "sw")
Label(root, text = "Averrage = ").grid(row = 1,column = 0 , stick = "sw")

name = Entry(root)
average = Entry(root)

def check_major():
    store_result = ""
    print("name  = " , name.get())
    print("average  = " , average.get())
    print("gender = " , gender.get())
    print("It = %d\n MT = %d\n Math = %d \n E-Ai = %d " %(it.get (),mt.get (), mh.get (), eai.get ()))
    tg = it.get()
    mg = mt.get()
    mag = mh.get()
    eag = eai.get()
    if tg == 1:
        store_result += "IT"
    if mg == 1:
       store_result += "MT"
    if mag == 1:
       store_result += "Math"
    if eag == 1:
       store_result += "E-AI"
    result.set("คุณได้เลือกวิชาเอกนี้" + store_result)
    pass



name.grid(row = 0,column = 1)
average.grid(row = 1,column = 1)

gender = StringVar()
Label(root, text  = "SEX = ").grid(row = 2,column  = 0,stick = "sw")
Radiobutton(root,text  = "Male  ",value = "male", variable = gender).grid(row = 2,column = 1,stick = "w")
Radiobutton(root,text  = "Female  ",value = "Female", variable = gender).grid(row = 2,column = 1,stick = "s")
#Radiobutton(root,text = "male =",value = "male", variable = gender).grid(row = 2,column = 1, stick ="w")
Checkbutton(root,text = "IT",variable = it) .grid(row = 3 , column = 1,stick = "w")
Checkbutton(root,text = "MT",variable = mt) .grid(row = 4 , column = 1,stick = "w")
Checkbutton(root,text = "MATH",variable = mh) .grid(row = 5 , column = 1,stick = "w")
Checkbutton(root,text = "E-AI",variable = eai) .grid(row = 6 , column = 1,stick = "w")

Button(root,text  = "OK", width  =6 , command  = check_major).grid(row = 7 , column = 1, stick = "w")
Button(root,text  = "Quit" ,width = 6,command   = quit).grid(row = 7,column  = 1 ,stick = "s")

Label (root,text = "คำตอบ = " ) .grid(row  = 8 ,column  = 0)
Label(root,textvariable = result).grid(row = 8 ,column  = 1)

root.mainloop()