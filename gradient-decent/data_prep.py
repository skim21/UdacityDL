
# coding: utf-8

# In[8]:

import numpy as np
import pandas as pd
import os

cur_dir = os.getcwd() 
print(cur_dir)
admissions = pd.read_csv(cur_dir + '/binary.csv')

# Make dummy variables for rank
data = pd.concat([admissions, pd.get_dummies(admissions['rank'], prefix='rank')], axis=1)
print(data.head())
data = data.drop('rank', axis=1)
print(data.head())


# In[11]:

# Standarize features
for field in ['gre', 'gpa']:
    mean, std = data[field].mean(), data[field].std()
    data.loc[:,field] = (data[field]-mean)/std
print(data.head())
    
# Split off random 10% of the data for testing
np.random.seed(42)
sample = np.random.choice(data.index, size=int(len(data)*0.9), replace=False)
data, test_data = data.ix[sample], data.drop(sample)
print(sample)

# Split into features and targets
features, targets = data.drop('admit', axis=1), data['admit']
features_test, targets_test = test_data.drop('admit', axis=1), test_data['admit']


# In[ ]:




# In[ ]:



