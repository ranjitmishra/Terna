# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:13:51 2018

@author: Cool
"""
#%%
import numpy as np
import pandas as pd

#%%
## Read input data file for analysis, perform descriptive analysis to understand the data

ecom = pd.read_csv('ecommerce.txt', sep = "\t") # .dropna()

ecom.shape

ecom.head()

ecom.describe()
ecom.dtypes
ecom.isnull().sum()
ecom.churn_status.value_counts()
ecom.groupby('churn_status').mean()
#%%
from sklearn import preprocessing

binConv = preprocessing.LabelEncoder()

# Convert churn variable to numeric and build a dummy variable
targets = binConv.fit_transform(ecom["churn_status"])
targets[1:10]
ecom.shape
cols = ecom.columns[1:9]

features = ecom[cols]
features.shape
#%%
## convert data to numpy array, Get target anf fetures split

ecom.churn_status = targets
ecom.describe()

ecomNP = np.array(ecom)

def targetFeatureSplit( data ):
    target = []
    features = []
    for item in data:
        target.append( item[0] )
        features.append( item[1:] )

    return target, features

target, features = targetFeatureSplit( ecomNP )

print(np.mean(target))
print(np.mean(features, axis = 0))
#%%
# Decision tree classifier

from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

feature_train, feature_test, target_train,\
 target_test = train_test_split(features, target, test_size=0.3, random_state = 42)

features_train = feature_train   #[:30]
labels_train   = target_train    #[:30]

clf = DecisionTreeClassifier(criterion = "gini", random_state = 42,
                               max_depth = 5, min_samples_leaf = 5)

clfFit = clf.fit(features_train,labels_train)
clfFit.score(feature_test,target_test)

y_pred = clf.predict(feature_test)

acc = accuracy_score(y_pred, target_test)
acc

#%%
## Visualize the tree
with open("ecom_tree.txt", "w") as f:
    f = tree.export_graphviz(clf, out_file=f)

## Code has been generated in ud-projects/tools. copy nad paste on http://www.webgraphviz.com/
#%%
