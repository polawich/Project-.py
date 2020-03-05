class allbmi:
    def __init__(self,weight,height):
        self.Weight = weight 
        self.Height = height
        self.bmi = ""
    def info (self):
        heiM = (self.Height / 100) ** 2
        self.bmi =(self.Weight / heiM)
        return self.bmi
    def cal (self,cal):
        if cal < 18.5 and cal >= 0:
            rs = ("นํ้าหนักตํ่ากว่าเกณฑ์")
        elif cal >= 18.5 and cal <= 22.9:
            rs = ("สมส่วน")
        elif cal >= 23.0 and cal <= 24.9:
            rs = ("นํ้าหนักเกิน")
        elif cal >= 25.0 and cal <= 29.9:
            rs = ("โรคอ้วน")
        elif cal >= 30.0:
            rs = ("โรคอ้วนอันตราย")
        return rs
    pass
ipname = str(input("ชื่อ: " ))
ipwht = int(input("นํ้าหนัก: "))
iphei = int(input("ส่วนสูง: "))
run = allbmi(ipwht,iphei)
print("\n","ชื่อ = ",ipname ,"\n","ส่วนสูง = ",ipwht,"\n","นํ้าหนัก = ",iphei,"\n","BMI = ",'%.2f'% run.info(),"\n","ภาวะเสี่ยงต่อโรค:",run.cal(int(run.info())))
