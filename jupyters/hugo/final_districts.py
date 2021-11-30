# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
### Library Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Script Imports
import utils

def cleanup():
    ### Import the loans file
    na_values= ['None', '?',]
    df = pd.read_csv('../../project/banking_data/district.csv', sep=';',na_values=na_values)

    df.isnull().sum()

    ### Replace null values in the '95 column for the ones on the '96 column
    #districts = utils.replace_null(df)

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

    districts = districts[cols]

    return districts


