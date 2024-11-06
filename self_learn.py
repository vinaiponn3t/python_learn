# create Class
class Employee:
    x = 10
    y = 25
    z = 'superpower'
    #create method
    def detail(self):
        self.name = 'vinaipon'
        self.surname = 'Onwan'
        print('program is running',self.name)
        print('value self of x:',self.x)

# create Object
emp1 = Employee()
print('=====')
emp1.detail()
print("ชื่อของพนักงาน :{}".format(emp1.z))