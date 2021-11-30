
### Library Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Script Imports
import utils

def cleanup(test = False):
    ### Import the trans file

    
    
    na_values= ['None', '?',]
    
    if test:
        df = pd.read_csv('../../project/banking_data/trans_test.csv', sep=';',na_values=na_values)
    else:
        df = pd.read_csv('../../project/banking_data/trans_train.csv', sep=';',na_values=na_values)
    


    ### Convert date format
    trans = utils.date_conversion(df,'date')


    ### Drop columns with too many missing values
    trans = utils.drop_null_columns(trans,0.4)


    ### Replace null values from the operation column for the most common occurence
    trans['operation'] = trans['operation'].fillna(trans['operation'].value_counts().idxmax())


    lower_bound = trans['balance'].quantile(.10)
    upper_bound = trans['balance'].quantile(.90)


    trans = trans[(trans['balance'] > lower_bound) & (trans['balance'] < upper_bound)]


    return trans


