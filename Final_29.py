from tkinter import*
root.title("Register Cutomer")
def Register():
    store_Answer = ""
    print("Name = ",name.get())
    print("Email = ",email.get())
    print("Address = ",address.get())
    print("Mobile = ",mobile.get())
    print("Name = %d,\nEmail =%d,\nAddress = %d,\nMobile = %d"%(om.get(),tm.get(),hm.get(),ym.get()))
    im = om.get()
    mm = tm.get()
    eam = hm.get()
    mam = ym.get()
    discount = 0
    s_type = Type.get()
    if im == 1:
        cost = 250 * 1
    if mm == 1:
        cost = 250 * 3
        if s_type == "student":
            discount = 10
        elif s_type == "official":
            discount = 5
        elif s_type == "general public":
            discount = 0
            pass
    if eam == 1:
        cost = 250 * 6
        if s_type == "student":
            discount = 15
        elif s_type == "official":
            discount = 1
        elif s_type == "general public":
            discount = 5
            pass
    if mam == 1:
        cost = 250 * 12
        if s_type == "student":
            discount = 20
        elif s_type == "official":
            discount = 15
        elif s_type == "general public":
            discount = 10
            pass
 
   
    Ans.set("ชื่อสมาชิก : {} \n ราคา : {} ".format(name.get(),(cost - (cost * discount / 100))))
 
root = Tk()
root.option_add("*Font","Consolas 24")
Label(root,text = "Name = ").grid(row = 0,column = 0,stick = "sw")
Label(root,text = "Email = ").grid(row = 1,column = 0,stick = "sw")
Label(root,text = "Address = ").grid(row = 2,column = 0,stick = "sw")
Label(root,text = "Mobile = ").grid(row = 3,column = 0,stick = "sw")
Label(root,text = "Monthly = ").grid(row = 4,column = 0,stick = "sw")
 
Ans = StringVar()
name = Entry(root)
email = Entry(root)
address = Entry(root)
mobile = Entry(root)
 
name.grid(row = 0,column = 1)
email.grid(row = 1,column = 1)
address.grid(row = 2,column = 1)
mobile.grid(row = 3,column = 1)
 
Type = StringVar()
Label(root, text = "Type = ").grid(row = 4,column = 2,stick = "sw")
Radiobutton(root,text = "Student",value = "student",variable = Type).grid(row = 4,column = 3,stick = "w")
Radiobutton(root,text = "Official",value = "official",variable = Type).grid(row = 5,column = 3,stick = "w")
Radiobutton(root,text = "General public",value = "general public",variable = Type).grid(row = 6,column = 3,stick = "w")
 
om = IntVar()
Checkbutton(root,text = "1 Month",variable = om).grid(row = 4,column = 1,stick = "w")
tm = IntVar()
Checkbutton(root,text = "3 Month",variable = tm).grid(row = 5,column = 1,stick = "w")
hm = IntVar()
Checkbutton(root,text = "6 Month",variable = hm).grid(row = 6,column = 1,stick = "w")
ym = IntVar()
Checkbutton(root,text = "12 Month",variable = ym).grid(row = 7,column = 1,stick = "w")
 
Button(root,text = "Register",width = 10,command = Register).grid(row = 8,column = 3,stick = "w")
Button(root,text = "QUIT",width = 10,command = quit).grid(row = 9,column = 3,stick = "w")
 
 
 
Label(root,text = "สมาชิค = ").grid(row = 9,column = 0)
Label(root,textvariable = Ans).grid(row = 9,column = 1)
root.mainloop()