# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:44:50 2020

@author: ASUS
"""


import numpy as np
import pandas as pd

df=pd.read_excel("KPMG_VI_New_raw_data_update_final.xlsx", sheet_name="Transactions") #we write sheet name here because pandas will not open the entire workbook with all sheets

dfhead=df.head() 

df.info()

df["product_first_sold_date"]=pd.to_datetime(df["product_first_sold_date"])

df["product_first_sold_date"]=pd.to_datetime(df["product_first_sold_date"]).dt.date

df.info()

dup=df.duplicated() 

df[dup].sum() 

isnull=df.isnull().sum()

df["customer_id"].duplicated().sum() 


df1=pd.read_excel("KPMG_VI_New_raw_data_update_final.xlsx", sheet_name="CustomerDemographic")

df1head=df1.head() 

df1.describe() 

df1.isnull().sum() 

df1=df1.drop("default", axis=1)

duplicatesindf1=df1.combined.duplicated()

