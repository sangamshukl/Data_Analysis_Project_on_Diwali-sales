#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data=pd.read_csv(r'Diwali Sales Data.csv',
                 encoding='unicode_escape',delimiter=" *, *")
data


# In[3]:


data.columns


# In[4]:


data.info()


# In[5]:


data['User_ID']=data['User_ID'].astype(int)
data.head(5)


# In[6]:


data.info()


# In[7]:


data.shape


# In[8]:


pd.isnull(data)


# In[9]:


data.drop(['Status','unnamed1'],axis=1,
          inplace=True)


# In[10]:


data


# In[11]:


#check the null values
pd.isnull(data).sum()


# In[12]:


data.shape


# In[13]:


#drop the null values
data.dropna(inplace=True)


# In[14]:


pd.isnull(data).sum()


# In[15]:


data.shape


# # Both are same 
# 
# data.dropna(inplace=True)
# 
# data_test=data.dropna()

# In[16]:


#change the datatype
data['Amount']=data['Amount'].astype('int')


# In[17]:


data['Amount'].dtypes


# In[18]:


data.columns


# In[19]:


# rename the columns using Dictnary 
# This change will not be save unless until we use --> inplace=True
data.rename(columns={'Marital_Status':'Shaadi','Amount':'Paisa','Age':'काल'})
data.head(2)


# In[20]:


data.head(2)


# In[21]:


# describe() method return description of the data in DataFrame (i.e: mean , count , std , etc)

data.describe()


# In[22]:


#use describe() for specific columns
data[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis
# 
# **Gender**

# In[23]:


data.columns


# In[24]:


sns.countplot(x= 'Gender',data=data)


# In[25]:


ax=sns.countplot(x= 'Gender',data=data)

for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


data.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[27]:


sales_gen=data.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Gender',y='Amount',data=sales_gen)

# from above graphs we can see that most of the buyers are females and even the purchase power of females are greater than men 
# **Age**

# In[28]:


ax=sns.countplot(data=data,x= 'Age Group',hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[29]:


sales_gen1=data.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Age Group',y='Amount',data=sales_gen1)


# from above grphs we can see that most of the buyers are of age  group between 25-35 yrs female

# **State**

# In[30]:


data.columns


# In[31]:


#total number of ordrs from top 10 states
sales_state=data.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x="State",y='Orders')


# In[32]:


#total amount/states from top 10 states

sales_states=data.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',
                                                            ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_states,x="State",y="Amount")


# from above graphs we can see that most of the order & total sales/amount are from U.P , Maharashtra and karnataka respectively

# **Marital Status**

# In[33]:


data.columns


# In[34]:


ax=sns.countplot(data=data,x='Marital_Status')

sns.set(rc={'figure.figsize':(15,15)})

for bars in ax.containers:
        ax.bar_label(bars)


# In[35]:


sales_state=data.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(5)

sns.set(rc={'figure.figsize':(15,15)})

sns.barplot(data=sales_state,x='Marital_Status',y='Amount',
           hue='Gender')


# *From above graphs we can see that most of the buyers are married (women) and they have high purchasing power*

# **Occuption**

# In[36]:


sns.set(rc={'figure.figsize':(18,5)})
ax=sns.countplot(data=data,x='Occupation')

for bar in ax.containers:
    ax.bar_label(bars)


# In[37]:


sales_state=data.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(20,10)})

sns.barplot(data=sales_state,x='Occupation',y='Amount')


# From above graphs we can see that most of the buyers are working in IT Aviation and Healthcare sectors

# **Product Category**

# In[38]:


data.columns


# In[39]:


sns.set(rc={'figure.figsize':(16,10)})

ax=sns.countplot(data=data,x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[40]:


sales_state=data.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',
                                                                         ascending=False).head(5)

sns.set(rc={'figure.figsize':(16,10)})

sns.barplot(data=sales_state,x='Product_Category',y='Amount')


# from above graphs we can see that most of the sold product are food , footwear and electronic

# In[41]:


sales_state=data.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',
                                                                         ascending=False).head(5)

sns.set(rc={'figure.figsize':(16,10)})

sns.barplot(data=sales_state,x='Product_ID',y='Orders')


# In[43]:


#top 10 most sold Product
sns.set(rc={'figure.figsize':(18,6)})
sns.barplot(data=sales_state,x='Product_ID',y='Orders')


# In[ ]:




