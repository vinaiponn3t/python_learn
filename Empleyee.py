# name & salary
class Employee:#การสร้าง class
    #def __init__(self):
        #print("default constructor")
    #สร้าง method
    def __init__(self,name,surename,salary,department):
        print("default constructor")
        self.name = name
        self.surename = surename
        self.salary = salary   
        self.department = department
    def showdata(self):
        print ("ชื่อพนักงาน = {}".format(self.name))
        print ("นามสกุล = {}".format(self.surename))
        print ("เงินเดือน = {}".format(self.salary))
        print ("ตำแหน่ง = {}".format(self.department))
#การสร้างวัตถุ
emp1 = Employee('ก้อง','สุดหล่อ','3000','ผู้จัดการ')
emp1.showdata()
#print(emp1)