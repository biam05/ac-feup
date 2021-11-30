# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Script Imports
import utils

def cleanup():
    ### Import the clients file
    na_values= ['None', '?',]
    df = pd.read_csv('../../project/banking_data/client.csv', sep=';',na_values=na_values)

    ### Date conversion with creation of gender column
    clients = utils.date_conversion_genders(df,'birth_number')

    ### Reordering Columns
    cols = clients.columns.tolist()
    cols = cols[0:2] + cols[3:4] + cols[2:3]
    clients = clients[cols]
    
    return clients


