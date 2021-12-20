# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
### Library Imports
import pandas as pd
import numpy as np
### Script Imports
import utils


# %%
### Clean Accounts

def clean_account():
    
    ### Import the loans file
    na_values= ['None', '?',]
    df = pd.read_csv('../banking_data/account.csv', sep=';',na_values=na_values)
    
    ### Date conversion
    return utils.date_conversion(df,'date')


# %%
def clean_card(test = False):
    ### Import the loans file
    na_values= ['None', '?',]
    if(test):
        df = pd.read_csv('../banking_data/card_test.csv', sep=';',na_values=na_values)
    else:
        df = pd.read_csv('../banking_data/card_train.csv', sep=';',na_values=na_values)

    return utils.date_conversion(df,'issued')


# %%
def clean_client():
    ### Import the clients file
    na_values= ['None', '?',]
    df = pd.read_csv('../banking_data/client.csv', sep=';',na_values=na_values)
    

    ### Date conversion with creation of gender column
    df = utils.date_conversion_genders(df,'birth_number')
    
    ### Reordering Columns
    cols = df.columns.tolist()
    cols = cols[0:2] + cols[3:4] + cols[2:3]
    return df[cols]


# %%
def clean_district():
    ### Import the loans file
    na_values= ['None', '?',]
    df = pd.read_csv('../banking_data/district.csv', sep=';',na_values=na_values)

    ### Replace null values in the '95 column for the ones on the '96 column
    districts = df.copy()
    districts["no. of commited crimes \'95 "] = districts["no. of commited crimes \'95 "].combine_first(districts["no. of commited crimes \'96 "])
    districts["unemploymant rate \'95 "] = districts["unemploymant rate \'95 "].combine_first(districts["unemploymant rate \'96 "])
    
    ### Added columns for crime analysis
    districts['crime_growth'] = districts["no. of commited crimes '96 "] - districts["no. of commited crimes '95 "]
    districts['total_crime'] = districts["no. of commited crimes '96 "] + districts["no. of commited crimes '95 "]

    ### Added column for uneployment growth analysis
    districts['unemploymant_growth'] = districts["unemploymant rate '96 "] - districts["unemploymant rate '95 "]

    ### Reorder columns
    cols = districts.columns.tolist()
    cols = cols[:13] + cols[-1:] + cols[13:-1]

    return districts[cols]    
    


# %%
def clean_loans(test=False):
    ### Import the loans file
    na_values= ['None', '?',]
    if(test):
        df = pd.read_csv('../banking_data/loan_test.csv', sep=';',na_values=na_values)
    else:
        df = pd.read_csv('../banking_data/loan_train.csv', sep=';',na_values=na_values)
    
    return utils.date_conversion(df,'date')


# %%
def clean_trans(test = False):
    ### Import the trans file
    
    na_values= ['None', '?',]
    
    if test:
        df = pd.read_csv('../banking_data/trans_test.csv', sep=';',na_values=na_values)
    else:
        df = pd.read_csv('../banking_data/trans_train.csv', sep=';',na_values=na_values)
    


    ### Convert date format
    trans = utils.date_conversion(df,'date')

    ### Drop columns with too many missing values
    trans = utils.drop_null_columns(trans,0.4)

    ### Replace null values from the operation column for the most common occurence
    trans['operation'] = trans['operation'].fillna(trans['operation'].value_counts().idxmax())
    
    return trans


