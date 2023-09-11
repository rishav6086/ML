#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


pip install pandas


# In[2]:


pip install numpy


# In[3]:


pip install seaborn


# In[4]:


import numpy


# In[5]:


import pandas as pd


# In[6]:


import seaborn as sns


# In[7]:


import sklearn


# In[8]:


pip install scikit.learn


# # ML

# In[13]:


from sklearn import tree
features=[[140,1],[130,1],[150,0],[170,0]]
labels=[0,0,1,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print(clf.predict([[150,0]]))


# In[ ]:




