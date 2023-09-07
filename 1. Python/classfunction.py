#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ageAadhar():
    
    def init(self):
        pass
        
    def ageCata(self):
        age=int(input("enter the age:"))
        if(age<=18):
            print("child")
        elif(age<=35):
            print("adult")
        elif(age<=55):
            print("citizen")
        else:
            print("senior citizen")

    def addition(self):
        num1=int(input("Enter the number1:"))
        num2=int(input("Enter the number2:"))
        add=num1+num2
        print(add)
    


