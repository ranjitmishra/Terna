# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 11:06:05 2018

@author: Cool
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
#%%
# read the data
creditHist = pd.read_csv("credithist.csv") # .dropna()
creditHist.shape
print(creditHist.columns)
creditHist.describe(include = 'all')

creditHist.dtypes

creditHist.isnull().sum()  # chaeck for null data
creditHist.Default.value_counts()       # Get the count of no/yes defaults
#%%
# use encoder to convert objects to integers
def dummyEncode(df):
        columnsToEncode = list(df.select_dtypes(include=['category','object']))
        le = LabelEncoder()
        for feature in columnsToEncode:
            try:
                df[feature] = le.fit_transform(df[feature])
            except:
                print('Error encoding '+feature)
        return df

credhist_transformed = dummyEncode(creditHist)
#%%
# Create dependent and independent variables
creditHist_array = np.array(credhist_transformed)
creditHist_array.shape
creditHist_array[0:5]
X, y = creditHist_array[:, 1:21], creditHist_array[:, 0]
X[0:5]
y[0:5]

class_0 = np.array(X[y == 0])
class_1 = np.array(X[y == 1])
class_0[1:10]
#%%
# Visualize input data
plt.figure()
plt.scatter(class_0[:, 0], class_0[:, 1], s=75, facecolors='red', 
        edgecolors='black', linewidth=1, marker='x')

plt.scatter(class_1[:, 0], class_1[:, 1], s=75, facecolors='white', 
        edgecolors='blue', linewidth=1, marker='o')
plt.title('Input Data')
plt.show()

X_train, X_test, y_train, y_test = cross_validation.train_test_split(
        X, y, test_size=0.25, random_state=5)
#%%
# Decision Trees classifier and acuracy score
params = {'random_state': 0, 'max_depth': 4}
classifier = DecisionTreeClassifier(**params)
classifier = classifier.fit(X_train, y_train)

y_test_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test_pred, y_test)

print("accuracy Score is: ", acc)
#%%