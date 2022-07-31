# Semester Dining Class
# Objects are created with semester name and year a the name
# Semester Dining Class Stores All Dining_Account objects
class SemesterDining:
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

# Dining_Account Class
class Dining_Account:
    def __init__(self):
        self.name = ''
        self.diningDollars=0.0
        self.swipes=0
        self.swipeStatus=None
        
    def setName(self,data):
        self.name = data
    def setDiningDollars(self,data):
        diningDollars = float(data)
        self.diningDollars=diningDollars
    
    def setSwipes(self,data):
        swipes = int(data)
        self.swipes = swipes
        
    def setSwipeStatus(self,data):
        swipeStatus = str(data)
        self.swipeStatus=swipeStatus
        
    def setAll(self,name,diningDollars,swipes,swipeStatus):
        self.setName(name)
        self.setDiningDollars(diningDollars)
        self.setSwipes(swipes)
        self.setSwipeStatus(swipeStatus)
        
    def getDiningDollars(self):
        return self.diningDollars
        
    def getSwipes(self):
        return self.swipes
        
    def getSwipeStatus(self):
        return self.swipeStatus
    
    def getAccountSummary(self):
        return 'Dining$:',self.getDiningDollars(),'Swipes:',self.getSwipes(),'Swipe Status:',self.getSwipeStatus()
        
    def chargeDiningDollars(self,amount):
        if self.diningDollars>0:
            self.diningDollars= self.diningDollars-float(amount)
        
    def addDiningDollars(self,amount):
        self.diningDollars= self.diningDollars+float(amount)
        
    def chargeSwipes(self,amount):
        self.swipes= self.swipes-int(amount)
        
def addingCharges(semester,studentAccount,chargeName,chargeAmount):
    studentAccount.addCharge(chargeName,chargeAmount)
    semester.addObject(studentAccount)

def addNewObjects(semester,diningAccount,name,diningDollars,swipes,swipeStatus):
    diningAccount.setAll(name,diningDollars,swipes,swipeStatus)
    semester.addObject(diningAccount)
    
def chargeDDollars(semester,diningAccount,amount):
    diningAccount.chargeDiningDollars(amount)
    semester.addObject(diningAccount)
    
def addDDollars(semester,diningAccount,amount):
    diningAccount.addDiningDollars(amount)
    semester.addObject(diningAccount)
    
def swipeDown(semester,diningAccount,swipes):
    diningAccount.chargeSwipes(swipes)
    semester.addObject(diningAccount)
    
# Creating Semester Object
FallDining19=SemesterDining()
# Creating Dining Account Objects
Kovenda=Dining_Account()
David=Dining_Account()

# Instantiate Dining Account Objects and Add them to Semester Dining
addNewObjects(FallDining19,Kovenda,'Kovenda',250,14,'Week')
addNewObjects(FallDining19,David,'David',200,19,'Week')

chargeDDollars(FallDining19,Kovenda,0)
chargeDDollars(FallDining19,Kovenda,18.60)
chargeDDollars(FallDining19,Kovenda,1.93)
chargeDDollars(FallDining19,Kovenda,13.63)
chargeDDollars(FallDining19,Kovenda,213.63)
chargeDDollars(FallDining19,Kovenda,13.63)

chargeDDollars(FallDining19,David,12)
chargeDDollars(FallDining19,David,1.60)
chargeDDollars(FallDining19,David,1.93)
chargeDDollars(FallDining19,David,1.63)
chargeDDollars(FallDining19,David,23.63)
chargeDDollars(FallDining19,David,3.63)

addDDollars(FallDining19,Kovenda,113.63)

addDDollars(FallDining19,David,31.63)

swipeDown(FallDining19,Kovenda,1)
swipeDown(FallDining19,Kovenda,1)
swipeDown(FallDining19,Kovenda,1)
swipeDown(FallDining19,Kovenda,1)

swipeDown(FallDining19,David,1)
swipeDown(FallDining19,David,1)
swipeDown(FallDining19,David,1)
swipeDown(FallDining19,David,1)
swipeDown(FallDining19,David,1)

