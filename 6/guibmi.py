from tkinter import *
def cal_bmi():
    h = float(entHight.get())
    w = float(entWeight.get())
    m = h/100
    bmi = w/(m**2)
    result = ""
    b.set(bmi)
    total = h+w
    #print("BMI = ",total)
    if bmi < 18.5 and bmi >= 0:
       result = "นั้าหนักตำกว่าเกณฑ์"
    elif bmi >= 18.5 and bmi <= 22.9:
        result = "สมส่วน"
    elif bmi >= 23.0 and bmi <= 24.9:
        result = "นํ้าหนักเกิน"
    elif bmi >= 25.0 and bmi <= 29.9:
        result = "โรคอ้วน"
    elif bmi >= 30.0:
        result = "โรคอ้วนอันตราย"
    sc.set(result)
admin =Tk()
admin.option_add("*Font","consolas 30") 
admin.title("BMI")
b = IntVar()
sc = StringVar()
Label(admin, text = "Hight = ").grid(row = 0, column = 0)
Label(admin, text = "Weight = ").grid(row = 1, column = 0)
Label(admin, textvariable = b ).grid(row = 2, column = 0)
Label(admin, textvariable = sc ).grid(row = 3, column = 0)
entHight = Entry(admin)
entWeight = Entry(admin)

entHight.grid(row = 0, column = 1 ) 
entWeight.grid(row = 1, column = 1)

Button(admin, text = "Calculate BMI",command = cal_bmi).grid(row = 4,column = 1)

admin.mainloop()
