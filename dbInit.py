from pymongo import MongoClient
from pprint import pprint
import csv
import pandas as pd


client = MongoClient('mongodb://localhost:27017/')

mydb = client.mydb
orders = mydb.orders

dblist = client.list_database_names()
if "mydb" in dblist:
  print("The database exists.")


print(mydb)


df = pd.read_csv('Test task - Orders.csv')
reader = csv.DictReader(df)

records_ = df.to_dict(orient = 'records')
result = orders.insert_many(records_ )

