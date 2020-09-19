# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:32:38 2020

@author: ASUS
"""

import numpy as np
import matplotlib as plt
import pandas as pd

data=pd.read_csv("Social_Network_Ads.csv")
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion = "entropy", random_state = 0)
dtc.fit(X_train, Y_train)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=10, criterion = "entropy", random_state = 0)
rfc.fit(X_train, Y_train)

y_pred = rfc.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(Y_test, y_pred))

from sklearn.metrics import accuracy_score
accuracy_score(Y_test, y_pred)

y2_pred=dtc.predict(X_test)


accuracy_score(Y_test, y2_pred)