#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from model import model 
import pandas as pd

class main():
    
    def __init__(self):
        self.model = model()
        
    def evaluate(self, test_file_address):
        
        test_file = pd.read_csv(test_file_address)
        
        return self.model.evaluate(test_file_address)


