class basic:
    def __init__(self,fristName,lastName):
        self.frstName = fristName
        self.LastName = lastName
    def getName(self):
        return self.FrstName +" "+ self.LastName
name1 = input('Enter Frist Name = ')
name2 = input('Enter Last Name = ')
b = basic(name1,name2)
print(b.getName())