#!/usr/bin/env python
# coding: utf-8

# In[67]:


#Importing pandas library
import pandas as pd

pd.options.display.width = 500
pd.options.display.max_columns = None


# In[68]:


#Reading CSV dataset
beers_dataset = pd.read_csv("D:/PythonExercise/craft-cans/beers.csv")
breweries_dataset = pd.read_csv("D:/PythonExercise/craft-cans/breweries.csv")
print(beers_dataset.head())


# In[69]:


#To display the columns of the dataset
beers_dataset.columns


# In[70]:


#updating "unnamed" to "ID"
beers_dataset.columns = ['ID', 'abv', 'ibu', 'id', 'name', 'style', 'brewery_id', 'ounces']
beers_dataset


# In[71]:


breweries_dataset.columns


# In[72]:


breweries_dataset.columns = ['ID', 'name', 'city', 'state']
breweries_dataset


# In[73]:


beers_dataset.info()


# In[74]:


breweries_dataset.info()


# In[75]:


beers_dataset.describe()


# In[76]:


breweries_dataset.describe()


# In[77]:


#Joining two datasets using key field
beers_and_breweries = pd.merge(beers_dataset,
                              breweries_dataset,
                              how = 'inner',
                              left_on = "brewery_id",
                              right_on = "ID",
                              sort = True,
                              suffixes = ('_beer', '_brewery'))
beers_and_breweries


# In[78]:


beers_dataset.dtypes


# In[79]:


breweries_dataset.dtypes


# In[80]:


beers_and_breweries.dtypes


# In[87]:


def get_var_category(series):
    unique_count = series.nunique(dropna = False)
    total_count = len(series)
    if pd.api.types.is_numeric_dtype(series):
        return 'Numerical'
    elif pd.api.types.is_datetime64_dtype(series):
        return 'Date'
    elif unique_count == total_count:
        return 'Text(unique)'
    else:
        return 'Catogorical'


# In[88]:


def print_categories(df):
    for column_name in df.columns:
        print(column_name, ': ' ,get_var_category(df[column_name]))


# In[89]:


print_categories(beers_dataset)


# In[90]:


print_categories(breweries_dataset)


# In[91]:


length = len(beers_dataset['ibu'])
print (length)


# In[92]:


count = beers_dataset['ibu'].count()
print (count)


# In[93]:


missing_values = length - count
print (missing_values)


# In[94]:


percentage_missing = float(missing_values/length)
percentage_missing = "{0:.1f}%".format(percentage_missing*100)
percentage_missing


# In[95]:


print ("Minimum value: ", beers_dataset['ibu'].min())


# In[96]:


print ("Maximum vlaue: ", beers_dataset['ibu'].max())


# In[97]:


print ("Mode: ", beers_dataset['ibu'].mode())


# In[98]:


print ("Mean: ", beers_dataset.mean())


# In[99]:


print ("Median: ", beers_dataset.median())


# In[100]:


print ("Standard_Dev: ", beers_dataset.std())


# In[101]:


Quantile = beers_dataset['ibu'].quantile([.25, .5, .75])
print (Quantile)


# In[102]:


import seaborn as sns
sns.set(color_codes = True)
sns.set_palette(sns.color_palette("muted"))

sns.distplot(beers_dataset['ibu'].dropna());


# In[59]:


beers_dataset[["abv", "ibu", "ounces"]].corr()


# In[ ]:




