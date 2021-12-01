
### Library Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Script Imports
import utils

### Import the loans file
def cleanup(test = False):
    na_values= ['None', '?',]
    
    
    if test:
        df = pd.read_csv('../../project/banking_data/card_test.csv', sep=';',na_values=na_values)
    else:
        df = pd.read_csv('../../project/banking_data/card_train.csv', sep=';',na_values=na_values)

    
    return utils.date_conversion(df,'issued')


