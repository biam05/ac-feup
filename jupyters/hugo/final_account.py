### Library Imports
import pandas as pd

### Script Imports
import utils

### Import the loans file

def cleanup():
    ### Read csv file
    na_values= ['None', '?',]
    df = pd.read_csv('../../project/banking_data/account.csv', sep=';',na_values=na_values)

    ### Date conversion
    return utils.date_conversion(df,'date')

