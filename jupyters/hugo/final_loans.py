### Library Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Script Imports
import utils

def cleanup(test = False):
    ### Import the loans file

    na_values= ['None', '?',]
    df = pd.read_csv('../../project/banking_data/loan_test.csv', sep=';',na_values=na_values)
    
    if test:
        df = pd.read_csv('../../project/banking_data/loan_test.csv', sep=';',na_values=na_values)
    else:
        df = pd.read_csv('../../project/banking_data/loan_train.csv', sep=';',na_values=na_values)

    ### Convert loan data to YYYY/MM/DD format
    return utils.date_conversion(df,'date')
    
    


