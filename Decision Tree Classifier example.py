#!/usr/bin/env python
# coding: utf-8



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data1 = pd.read_csv('Social_Network_Ads.csv')

X = data1.iloc[:, :-1].values
Y = data1.iloc[:, -1].values



from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state = 1)



from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion = "entropy", random_state = 0)
dtc.fit(X_train, Y_train)



y_pred = dtc.predict(X_test)

y_pred


Y_test

from sklearn.metrics import classification_report
print(classification_report(Y_test, y_pred))

