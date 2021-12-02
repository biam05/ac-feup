### Library Imports
import pandas as pd
import pandasql as ps


### Script Imports
import utils
import final_account
import final_card
import final_client
import final_districts
import final_loans
import final_trans


### Get all dataframes

accounts = final_account.cleanup()
card = final_card.cleanup()
clients = final_client.cleanup()
districts = final_districts.cleanup()
loans = final_loans.cleanup()
trans = final_trans.cleanup()
disp = pd.read_csv('../../project/banking_data/disp.csv', sep=';')