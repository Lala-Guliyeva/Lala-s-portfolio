#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('Position_Salaries.csv')


# In[2]:


data1


# In[3]:


X = data1.iloc[:, 1:-1].values
Y = data1.iloc[:, -1].values


# In[4]:


X


# In[5]:


Y


# In[6]:



from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor(random_state = 0)
dtr.fit(X, Y)


# In[11]:


dtr.predict([[12]])


# In[ ]:




