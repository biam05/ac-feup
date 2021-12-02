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

def cleanup(test=False):
    
    accounts = final_account.cleanup()
    card = final_card.cleanup(test)
    clients = final_client.cleanup()
    districts = final_districts.cleanup()
    loans = final_loans.cleanup(test)
    trans = final_trans.cleanup(test)
    disp = pd.read_csv('../../project/banking_data/disp.csv', sep=';')
    
    ### Merge everything with sequel queries
    
    df = loans.copy()

    ### Merge accounts
    df = df.merge(accounts, how='left', on="account_id")
    df = df.rename(columns={"date_x": "loan_date", "date_y" : "account_date"})

    ### Merge Districts 
    distrs = districts.rename(columns={"code ": "district_id"})
    df = df.merge(distrs, how='left', on="district_id")

    ### Merge Clients
    # clts = clients.drop(columns=['district_id'])
    df = df.merge(clients, how='left', on=["district_id"])

    ## Merge transactions
    trans2 = trans.rename(columns={"type": "trans_type" , "amount":"trans_ammount"})
    df = df.merge(trans2, how='left', on="account_id")


    # ### Create copy
    # df = loans.copy()

    # ### Merge accounts
    # df = df.merge(accounts, how='left', on="account_id")
    # df = df.rename(columns={"date_x": "loan_date", "date_y" : "account_date"})

    # ### Merge Disp
    # ### Mover para cleanup
    # q1 = "SELECT * FROM disp WHERE Type='OWNER'"
    # disp = ps.sqldf(q1)
    # df = df.merge(disp, how='left', on="account_id")

    # ### Merge Clients
    # clts = clients.drop(columns=['district_id'])
    # df = df.merge(clts, how='left', on="client_id")

    # ### Merge Districts 
    # distrs = districts.rename(columns={"code ": "district_id"})
    # df = df.merge(distrs, how='left', on="district_id")

    # ### Merge transactions
    # trans2 = trans.rename(columns={"type": "trans_type" , "amount":"trans_ammount"})
    # df = df.merge(trans2, how='left', on="account_id")

    # # ### Merge Card
    # # ## TODO: Rename issue column to date_something
    # # card = card.rename(columns={"type": "type_card"})
    # # df = df.merge(card, how='left', on="disp_id")
    
    return df



# def df_normalize(df):
    

def normalize_category(df):
    
    cp = df.copy()
    columns = cp.columns
    
    for column in columns:
        if(cp[column].dtypes != 'int64' and cp[column].dtypes != 'float64' and  cp[column].dtypes != 'int32' and  cp[column].dtypes != 'float32'):
            cp = utils.normalization(cp,column)
    
    return cp
            
    


