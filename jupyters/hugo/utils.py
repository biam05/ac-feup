# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
# ### Required Imports
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# client = pd.read_csv('../../project/banking_data/client.csv', sep=';')
# loan = pd.read_csv('../../project/banking_data/loan_train.csv', sep=';')

# ### Testing date conversion
# #client = date_conversion_genders(client,'birth_number')
# #loan = date_conversion(loan,'date')


# %%
### Convert numerical date to datetime formats
from datetime import datetime

def date_conversion(df,column,dt_format = '%d-%m-%Y'):
    df_copy = df.copy()
    date = df_copy[column]                                                             # Get the actual column
    date = date.astype(str)                                                            # Convert to string to add the century
    date = '19' + date                                                                 # Add the century value
    df_copy[column] = date.apply(lambda x: (datetime.strptime(x,'%Y%m%d')).strftime(dt_format))   # Convert to the desired date format

    return df_copy


def date_conversion_genders(df,column,dt_format = '%d-%m-%Y'):

    df_copy = df.copy()
    date = df_copy[column]                                            # Get the actual column
    date = date.astype(str)                                      # Convert to string to add the century
    date = '19' + date                                           # Add the century value

    ### Get the monts value with gender
    lst = []
    for item in date:
        lst.append(item[4:6])
        
    months = []
    gender = [] 
    for item in lst:
        if(int(item) > 50):
            months.append(int(item)- 50)
            gender.append('female')
        else:
            months.append(int(item))
            gender.append('male')
            
    ### Replace the old month values
    for i in range(len(date)):
        if gender[i] == 'female':
            date[i] = str(int(date[i])-5000)

    df_copy[column] = date.apply(lambda x: (datetime.strptime(x,'%Y%m%d')).strftime(dt_format))
    df_copy["gender"] = gender

    return df_copy



     


# %%
def replace_null(df):
    return df.fillna(df.median())
    


# %%
from sklearn import preprocessing

def encode_strings(df,column):

    copy = df.copy()
    encoder = preprocessing.LabelEncoder()
    encoder.fit(copy[column].unique())
    copy[column] = encoder.transform(copy[column])

    return copy
    


# %%
### Drop columns with percentage of nulls that surpasses the provided limit
def drop_null_columns(df,limit = 0.7):
    return df[df.columns[df.isnull().mean() < limit]]

### Drop rows with percentage of nulls that surpasses the provided limit
def drop_null_rows(df,limit = 0.5):
    return df.loc[df.isnull().mean() < limit]


