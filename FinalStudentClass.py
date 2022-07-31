# Semester Class
# Objects are created with semester name and year a the name
# Semester Class Stores All Student_Account objects
class Semester:
    def __init__(self):
        self.student_names = [] 
        self.accountSummary = [0]
        
    def put(self,key,data):
        if key in self.student_names:
            self.putCharge(key,data)
        else:
            self.student_names.append(key)
            self.accountSummary.append(0)
            self.putCharge(key,data)
        
    def putCharge(self,key,data):
        item = key
        list1 = self.student_names
        place = self.getIndex(list1,item)
        self.accountSummary[place]= data
        
    def get(self,key):
        result = 0
        
        if key in self.student_names:
            place = self.getIndex(self.student_names,key)
            result= self.accountSummary[place]
        return result
                
    def addObject(self,data):
        self.put(data.name,data.getAccountSummary())    
        
    def getIndex(self,list1,itme):
        return list1.index(itme)


# Student_Account Class
# This class is used to create new student account objects
class Student_Account():
    def __init__(self):
        self.name = ''
        self.chargeName = []
        self.chargeAmount = []

    def put(self,key,data):
        self.chargeName.append(key)
        self.chargeAmount.append(float(data))
        
    def getChargeAmount(self,key):
        if key in self.chargeName:
            index = self.chargeName.index(key)
            amount = self.chargeAmount[index]
        else:
            amount = 0
        return amount
        
    def getAccountSummary(self):
        key = self.chargeName[0]
        balance = 0
        ChargeName_list = []
        ChargeAmount_list = []
        account_summary = {}
        index = self.chargeName.index(key)
        ChargeName_list = self.chargeName
        ChargeAmount_list = self.chargeAmount
        for x in range(len(ChargeName_list)):
            account_summary[ChargeName_list[x]]=ChargeAmount_list[x]
        for y in account_summary.values():
            balance = balance + x
        return 'Name:',self.name,"Balance:", balance,'account summary',account_summary
        
    def addCharge(self,chargeName,chargeAmount):
        self.put(chargeName,chargeAmount)
        
    def setName(self,name):
        self.name = name

def addingCharges(semester,studentAccount,chargeName,chargeAmount):
    studentAccount.addCharge(chargeName,chargeAmount)
    semester.addObject(studentAccount)




# Creating Semester Object
Fall19=Semester()

# Createing Student Account objects
Kovenda=Student_Account()
Kovenda.setName('Kovenda')
Ben=Student_Account()
Ben.setName('Ben')


# Adding Charges to Student Account objects
addingCharges(Fall19,Kovenda,'tacos',-6)
addingCharges(Fall19,Kovenda,'Fees',2500)
addingCharges(Fall19,Kovenda,'Fs',25)
addingCharges(Fall19,Kovenda,'Set',-500)
addingCharges(Fall19,Kovenda,'Rests',2)
addingCharges(Fall19,Kovenda,'Press',-10)

addingCharges(Fall19,Ben,'tacos',-6)
addingCharges(Fall19,Ben,'Fees',2500)
addingCharges(Fall19,Ben,'Fs',25)
addingCharges(Fall19,Ben,'Set',-500)
addingCharges(Fall19,Ben,'Rests',2)
addingCharges(Fall19,Ben,'Press',-10)