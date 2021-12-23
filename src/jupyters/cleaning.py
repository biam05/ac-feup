# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
### Library Imports
import pandas as pd
import numpy as np
import sqlite3
### Script Imports
import utils

# %%
def pd_account(con):
    return pd.read_sql_query("SELECT * from account", con)

def pd_card_test(con):
    return pd.read_sql_query("SELECT * from card_test", con)

def pd_card_train(con):
    return pd.read_sql_query("SELECT * from card_train", con)

def pd_client(con):
    return pd.read_sql_query("SELECT * from client", con)

def pd_disp(con):
    return pd.read_sql_query("SELECT * from disp", con)

def pd_district(con):
    p = pd.read_sql_query("SELECT * from district", con)
    return p.replace('?', None)

def pd_loan_test(con):
    return pd.read_sql_query("SELECT * from loan_test", con)

def pd_loan_train(con):
    return pd.read_sql_query("SELECT * from loan_train", con)

def pd_trans_test(con):
    return pd.read_sql_query("SELECT * from trans_test", con)

def pd_trans_train(con):
    return pd.read_sql_query("SELECT * from trans_train", con)

# %%
### Clean Accounts

def clean_account(con):
    
    ### Import the loans file
    na_values= ['None', '?',]
    df = pd_account(con)
    
    ### Date conversion
    return utils.date_conversion(df,'date')


# %%
def clean_card(con, test = False):
    ### Import the loans file
    na_values= ['None', '?',]
    if(test):
        df = pd_card_test(con)
    else:
        df = pd_card_train(con)

    return utils.date_conversion(df,'issued')


# %%
def clean_client(con):
    ### Import the clients file
    na_values= ['None', '?',]
    df = pd_client(con)

    ### Date conversion with creation of gender column
    df = utils.date_conversion_genders(df,'birth_number')
    
    ### Reordering Columns
    cols = df.columns.tolist()
    cols = cols[0:2] + cols[3:4] + cols[2:3]
    return df[cols]


# %%
def clean_district(con):
    ### Import the loans file
    df = pd_district(con)


    ### Replace null values in the '95 column for the ones on the '96 column
    districts = df.copy()
    districts["no. of commited crimes '95"] = districts["no. of commited crimes '95"].combine_first(districts["no. of commited crimes '96"])
    districts["unemploymant rate '95"] = districts["unemploymant rate '95"].combine_first(districts["unemploymant rate '96"])
    
    ### Added columns for crime analysis
    districts['crime_growth'] = pd.to_numeric(districts["no. of commited crimes '96"]) - pd.to_numeric(districts["no. of commited crimes '95"])
    districts['total_crime'] = pd.to_numeric(districts["no. of commited crimes '96"]) + pd.to_numeric(districts["no. of commited crimes '95"])

    ### Added column for uneployment growth analysis
    districts['unemploymant_growth'] = pd.to_numeric(districts["unemploymant rate '96"]) - pd.to_numeric(districts["unemploymant rate '95"])

    ### Reorder columns
    cols = districts.columns.tolist()
    cols = cols[:13] + cols[-1:] + cols[13:-1]

    return districts[cols]    
    


# %%
def clean_loans(con, test=False):
    ### Import the loans file
    na_values= ['None', '?',]
    if(test):
        df = pd_loan_test(con)
    else:
        df = pd_loan_train(con)
    
    return utils.date_conversion(df,'date')


# %%
def clean_trans(con ,test = False):
    ### Import the trans file
    
    na_values= ['None', '?',]
    
    if test:
        df = pd_trans_test(con)
    else:
        df = pd_trans_train(con)
    


    ### Convert date format
    trans = utils.date_conversion(df,'date')

    ### Drop columns with too many missing values
    trans = utils.drop_null_columns(trans,0.4)

    ### Replace null values from the operation column for the most common occurence
    trans['operation'] = trans['operation'].fillna(trans['operation'].value_counts().idxmax())
    
    return trans


