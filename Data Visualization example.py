#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Matplotlib library
from matplotlib import pyplot as plt

# Line Plot
x = [1,2,3]
y = [1,2,3]
z = [1,4,9]

plt.plot(x,y, label = 'xy', linewidth = 3.0)
plt.plot(x,z, label = 'xz', linewidth = 2.0)
plt.title("My first PLot", fontsize = 20)
plt.xlabel("x", fontsize = 15)
plt.ylabel("y", fontsize = 15)
plt.legend(fontsize = 17)
plt.show()


# In[7]:


# Bar Plot
x = [1,2,3]
y = [1,2,3]

barl = plt.bar(x,y)
barl[1].set_color('r')
plt.show()


# In[8]:


# Bar Plot 2
import pandas as pd
data = {'2010':{1:100, 2:150, 3:200}, '2015':{1:20, 2:50, 3:40}, '2020':{1:100, 2:75, 3:40}}
data


# In[9]:


data = pd.DataFrame(data)
data


# In[11]:


data.plot(kind = 'bar')
plt.show()


# In[12]:


# Scatter Plot 
plt.scatter(x,y)
plt.show()


# In[15]:


data2 = pd.read_csv("exams.csv")
data2
data2.plot.scatter(x = 'exam_1', y = 'exam_2')
plt.show()


# In[19]:


df = pd.read_csv("full_data.csv")
df = df.tail(10)
df


# In[22]:


plt.plot(df['total_deaths'], df['date'], label = "total")
plt.plot(df['biweekly_deaths'], df['date'], label = "biweekly")
plt.title("Covid-19")
plt.show()


# In[59]:


# Pie Chart
labels = 'Germany', 'Azerbaijan', 'Japan', 'Turkey'
number = [150, 310, 45, 100]
total_d = [5, 8, 10, 5]


# In[60]:


exp = (0.1, 0.1, 0, 0)
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.pie(number, explode=exp, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax2.pie(total_d, explode=exp, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.axis('equal')
plt.show()


# In[ ]:





# In[ ]:




