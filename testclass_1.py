#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Animal:
    """A single attempt to medel a dog"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('successfully executed and called out ')
        
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"    {self.name} is now sitting ")
        
    def roll_over(self):
        """simulate a dog rollover in response to a command"""
        print(f" {self.name} rolled over")

