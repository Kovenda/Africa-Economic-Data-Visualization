#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Meal Plan Class
class Meal_Plan:
    def __init__(self):
        #self.size = 11
        self.plan_names = ['plan_name'] 
        self.data = [['Dining_dollars', 'Swipes','Swipe_status']] 
# Enter all available meal plans
    def put(self,key,data):
        self.plan_names.append(key)
        self.data.append(data.split(' '))
        
        
        
# display all the available meal plans with the relivent information        
# get the information for a meal plan requested user
    def get(self,key):
        result = []
        position = 1
        if key in self.plan_names:
            index = self.plan_names.index(key)
            meal_status_list = self.data[index]
            meal_status_definition=self.data[0]
            string1 = self.plan_names[0]+ ':'+key
            string2 = meal_status_definition[0] + ':'+meal_status_list[0]
            string3 = meal_status_definition[1] + ':'+meal_status_list[1]
            string4 = meal_status_definition[2] + ':'+meal_status_list[2]
            result = [string1,string2,string3,string4]
        return result 
            
                

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


# In[14]:


# Creating Meal Plans
H=Meal_Plan()
H['Ultimate']="100 1 hour"
H['Full Board']="200 19 week"
H['Weekly Deal']="250 14 week"
H['Semester Plan 1']="200 225 semester"
H['Semester Plan 2']="175 325 semester"
H['Semester Plan 3']="120 600 semester"


print(H['Semester Plan 1'])
# In[ ]:



#!/usr/bin/env python
# coding: utf-8

# In[5]:


