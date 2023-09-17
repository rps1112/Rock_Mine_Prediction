#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


sd=pd.read_csv(r"C:\Users\rpsie\Downloads\Projects\ML Projects\sonar_data.csv",header=None)


# In[3]:


sd.head(10)


# In[4]:


sd.shape


# In[5]:


sd.info()


# In[6]:


sd.describe()


# In[7]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[8]:


sd[60].value_counts()


# In[9]:


sd.groupby(60).mean()


# In[10]:


x=sd.drop(60,axis=1)
y=sd[60]
print(x)
print(y)


# ## Train Model

# In[11]:


x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=30,test_size=0.2,stratify=y)
print('dependent variable train size:',len(x_train))
print('dependent variable test size:',len(x_test))
print('independent variable train size:',len(y_train))
print('independent variable test size:',len(x_test))


# In[12]:


model=LogisticRegression()
model.fit(x_train,y_train)


# In[13]:


y_train_pred=model.predict(x_train)
train_accuracy=accuracy_score(y_train_pred,y_train)
train_accuracy


# In[14]:


y_test_pred=model.predict(x_test)
test_accuracy=accuracy_score(y_test_pred,y_test)
test_accuracy


# ## Check Prediction

# In[38]:


input=(
0.0731,0.1249,0.1665,0.1496,0.1443,0.2770,0.2555,0.1712,0.0466,0.1114,0.1739,0.3160,0.3249,0.2164,0.2031,0.2580,0.1796,0.2422,0.3609,0.1810,0.2604,0.6572,0.9734,0.9757,0.8079,0.6521,0.4915,0.5363,0.7649,0.5250,0.5101,0.4219,0.4160,0.1906,0.0223,0.4219,0.5496,0.2483,0.2034,0.2729,0.2837,0.4463,0.3178,0.0807,0.1192,0.2134,0.3241,0.2945,0.1474,0.0211,0.0361,0.0444,0.0230,0.0290,0.0141,0.0161,0.0177,0.0194,0.0207,0.0057
)
array=np.array(input)
reshaped_array=array.reshape(1,-1)
prediction=model.predict(reshaped_array)
print('The object detected is:',prediction)


# In[ ]:




