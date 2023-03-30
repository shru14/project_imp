#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[9]:


pd.__version__


# In[13]:


url = r'C:\Users\Ojaswi\Desktop\participant_invites_2023-03-25_16.00.csv'
df = pd.read_csv(url, sep='|')
df


# In[17]:


url = r'C:\Users\Ojaswi\Desktop\TPC Mumbai_Triggered IDS.xlsx'
df1 = pd.read_excel(url)
df1


# In[19]:


df2 = df[~df['CANo'].isin(df1['Triggered IDs'])] 
df2


# In[25]:


df2.to_csv(r'C:\Users\Ojaswi\Desktop\participant_invites_2023-03-30_16.00.csv', index=False, sep="|")


# In[ ]:




