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

# Part 2

import pandas as pd

import matplotlib as plt

dftrans=pd.read_excel("KPMG_VI_New_raw_data_update_final (2)(AutoRecovered).xlsx", sheet_name="Transactions")

X = dftrans.iloc[:, 1:-1].values

Y = dftrans.iloc[:, -1].values

import numpy as np

def split_train_test(data,test_ratio):
    
    shuffled_indices=np.random.permutation(len(data))
    
    test_set_size=int(len(data) * test_ratio)
    
    test_indices=shuffled_indices[:test_set_size:]
    
    train_indices=shuffled_indices[test_set_size:]
    
    return data.iloc[train_indices],data.iloc[test_indices]
    

from zlib import crc32

def test_set_check(identifier, test_ratio):

    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio*2**32

def split_train_test_by_id(data, test_ratio, id_column):

    ids=data[id_column]
    
    in_test_set=ids.apply(lambda id: test_set_check(id_, test_ratio))

    return data.loc[~in_test_set],data.loc[in_test_set]

from sklearn.model_selection import train_test_split

train_set,test_set=train_test_split(dftrans, test_size=0.2, random_state=42) 

dftrans=train_set.copy()


import matplotlib.pyplot as plt

dftrans.plot(kind="scatter", x="customer_id", y="profit_per_customer", alpha=0.2,
              s=dftrans["profit_per_customer"]/300, label="", figsize=(10,5)) 
plt.legend()

corr_matrix=dftrans.corr()

correlation_matrix=corr_matrix["profit_per_customer"].sort_values(ascending=False)

correlation_matrix=corr_matrix["profit_per_customer"].sort_values(ascending=False)


dftrans_labels=train_set["profit_per_customer"].copy()

isnull=dftrans.isnull().sum()

dftrans.isnull().sum()

dftrans=dftrans.drop("online_order", axis=1) 

dftrans.dropna(subset = ["brand", "product_line", "product_class", "product_size","profit","profit_per_customer","profit_per_customer", "standard_cost", "past_3_years_bike_related_purchases", "past_3_years_bike_related_purchases_modified"], inplace=True) 

dftrans.isnull().sum() 

dftrans.dropna(subset = ["address","postcode", "state", "country", "property_valuation"])
                             
dftrans.drop(["country","address", "postcode", "deceased_indicator", "job_industry_category"], axis=1)                             
                                                          
dftrans=train_set.drop("profit_per_customer", axis=1) 

from sklearn.preprocessing import OrdinalEncoder 

ordinal_encoder=OrdinalEncoder()

X[:, 6:10] = ordinal_encoder.fit_transform(X[:, 6:10]) 

enc = OrdinalEncoder()

enc.fit(dftrans[["order_status","brand", "product_line", "product_class", "product_size", "gender"]])

dftrans[["online_status","brand", "product_line", "product_class", "product_size", "gender"]] = enc.transform(dftrans[["order_status","brand", "product_line", "product_class", "product_size", "gender"]])

from sklearn.preprocessing import OneHotEncoder

cat_encoder=OneHotEncoder()

X[:, -1] = cat_encoder.fit_transform(X[:, -1])

X[:, -1] = ordinal_encoder.fit_transform(X[:, -1])
