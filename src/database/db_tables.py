import csv, sqlite3
import pandas as pd

## Functions to create the tables and drop them if they alreadt exist in the database

def ct_account():
    cur.execute("DROP TABLE IF EXISTS account")
    cur.execute("CREATE TABLE account (account_id, district_id, frequency, date)")

def ct_card_test():
    cur.execute("DROP TABLE IF EXISTS card_test")
    cur.execute("CREATE TABLE card_test(card_id, disp_id, type, issued)")

def ct_card_train():
    cur.execute("DROP TABLE IF EXISTS card_train")
    cur.execute("CREATE TABLE card_train (card_id, disp_id, type, issued)")

def ct_client():
    cur.execute("DROP TABLE IF EXISTS client")
    cur.execute("CREATE TABLE client (client_id, birth_number, district_id)")

def ct_disp():
    cur.execute("DROP TABLE IF EXISTS disp")
    cur.execute("CREATE TABLE disp (disp_id, client_id, account_id, type)")

def ct_district():
    cur.execute("DROP TABLE IF EXISTS district")
    cur.execute("CREATE TABLE district (code, name, region, \"no. of inhabitants\", \"no. of municipalities with inhabitants < 499\", \"no. of municipalities with inhabitants 500-1999\", \"no. of municipalities with inhabitants 2000-9999\", \"no. of municipalities with inhabitants >10000\", \"no. of cities\", \"ratio of urban inhabitants\", \"average salary\", \"unemploymant rate '95\", \"unemploymant rate '96\", \"no. of enterpreneurs per 1000 inhabitants\", \"no. of commited crimes '95\", \"no. of commited crimes '96\")")

def ct_loan_test():
    cur.execute("DROP TABLE IF EXISTS loan_test")
    cur.execute("CREATE TABLE loan_test (loan_id, account_id, date, amount, duration, payments, status)")

def ct_loan_train():
    cur.execute("DROP TABLE IF EXISTS loan_train")
    cur.execute("CREATE TABLE loan_train (loan_id, account_id, date, amount, duration, payments, status)")

def ct_trans_test():
    cur.execute("DROP TABLE IF EXISTS trans_test")
    cur.execute("CREATE TABLE trans_test (trans_id, account_id, date, type, operation, amount, balance, k_symbol, bank, account)")

def ct_trans_train():
    cur.execute("DROP TABLE IF EXISTS trans_train")
    cur.execute("CREATE TABLE trans_train (trans_id, account_id, date, type, operation, amount, balance, k_symbol, bank, account)")

##########################################################################

## Functions to insert values into already created tables from the database 

def account():
    with open('../banking_data/account.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['account_id'], i['district_id'], i['frequency'], i['date']) for i in dr]

    cur.executemany("INSERT INTO account (account_id, district_id, frequency, date) VALUES (?, ?, ?, ?);", to_db)
    con.commit()

def card_test():
    with open('../banking_data/card_test.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['card_id'], i['disp_id'], i['type'], i['issued']) for i in dr]

    cur.executemany("INSERT INTO card_test (card_id, disp_id, type, issued) VALUES (?, ?, ?, ?);", to_db)
    con.commit()

def card_train():
    with open('../banking_data/card_train.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['card_id'], i['disp_id'], i['type'], i['issued']) for i in dr]

    cur.executemany("INSERT INTO card_train (card_id, disp_id, type, issued) VALUES (?, ?, ?, ?);", to_db)
    con.commit()

def client():
    with open('../banking_data/client.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['client_id'], i['birth_number'], i['district_id']) for i in dr]

    cur.executemany("INSERT INTO client (client_id, birth_number, district_id) VALUES (?, ?, ?);", to_db)
    con.commit()

def disp():
    with open('../banking_data/disp.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['disp_id'], i['client_id'], i['account_id'], i['type']) for i in dr]

    cur.executemany("INSERT INTO disp (disp_id, client_id, account_id, type) VALUES (?, ?, ?, ?);", to_db)
    con.commit()

def district():
    with open('../banking_data/district.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['code '], i['name '], i['region'], i['no. of inhabitants'], i['no. of municipalities with inhabitants < 499 '], i['no. of municipalities with inhabitants 500-1999'], i['no. of municipalities with inhabitants 2000-9999 '], i['no. of municipalities with inhabitants >10000 '], i['no. of cities '], i['ratio of urban inhabitants '], i['average salary '], i['unemploymant rate \'95 '], i['unemploymant rate \'96 '], i['no. of enterpreneurs per 1000 inhabitants '], i['no. of commited crimes \'95 '], i['no. of commited crimes \'96 ']) for i in dr]

    cur.executemany("INSERT INTO district (code, name, region, \"no. of inhabitants\", \"no. of municipalities with inhabitants < 499\", \"no. of municipalities with inhabitants 500-1999\", \"no. of municipalities with inhabitants 2000-9999\", \"no. of municipalities with inhabitants >10000\", \"no. of cities\", \"ratio of urban inhabitants\", \"average salary\", \"unemploymant rate '95\", \"unemploymant rate '96\", \"no. of enterpreneurs per 1000 inhabitants\", \"no. of commited crimes '95\", \"no. of commited crimes '96\") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    con.commit()

def loan_test():
    with open('../banking_data/loan_test.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['loan_id'], i['account_id'], i['date'], i['amount'], i['duration'], i['payments'], i['status']) for i in dr]

    cur.executemany("INSERT INTO loan_test (loan_id, account_id, date, amount, duration, payments, status) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
    con.commit()

def loan_train():
    with open('../banking_data/loan_train.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['loan_id'], i['account_id'], i['date'], i['amount'], i['duration'], i['payments'], i['status']) for i in dr]

    cur.executemany("INSERT INTO loan_train (loan_id, account_id, date, amount, duration, payments, status) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
    con.commit()

def trans_test():
    with open('../banking_data/trans_test.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['trans_id'], i['account_id'], i['date'], i['type'], i['operation'], i['amount'], i['balance'], i['k_symbol'], i['bank'], i['account']) for i in dr]

    cur.executemany("INSERT INTO trans_test (trans_id, account_id, date, type, operation, amount, balance, k_symbol, bank, account) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    con.commit()

def trans_train():
    with open('../banking_data/trans_train.csv','r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['trans_id'], i['account_id'], i['date'], i['type'], i['operation'], i['amount'], i['balance'], i['k_symbol'], i['bank'], i['account']) for i in dr]

    cur.executemany("INSERT INTO trans_train (trans_id, account_id, date, type, operation, amount, balance, k_symbol, bank, account) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    con.commit()
    

##########################################################################

def create_tables():
    ct_account()
    ct_card_test()
    ct_card_train()
    ct_client()
    ct_disp()
    ct_district()
    ct_loan_test()
    ct_loan_train()
    ct_trans_test()
    ct_trans_train()
    return

def insert_into_tables():
    account()
    card_test()
    card_train()
    client()
    disp()
    district()
    loan_test()
    loan_train()
    trans_test()
    trans_train()

##########################################################################

con = sqlite3.connect("banking_data")
cur = con.cursor()

create_tables()
insert_into_tables()

con.close()