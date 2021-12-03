### Library Imports
import pandas as pd

### Script Imports
import utils


### Get all dataframes

accounts = final_account.cleanup()
card = final_card.cleanup()
client = final_client.cleanup()
districts = final_districts.cleanup()
loans = final_loans.cleanup()
trans = final_trans.cleanup()


### Merge everything with sequel queries

loans.merge(accounts, left_on='account_id')

print(loans)