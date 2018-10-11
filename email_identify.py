#!/usr/bin/python

""" 
    This is the code to accompany the project 3 (decision tree) mini-project for AI.
    Use a Decision Tree to identify emails by author:    
    Author Sara is labeled 0
    Author Chris is labeled 1
"""
    
#import sys
#sys.path.append("../tools/")

import pickle
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif

#words_file = "../tools/word_data.pkl", authors_file="../tools/email_authors.pkl"

words_file = "word_data.pkl"
authors_file= "email_authors.pkl"
authors_file_handler = open(authors_file, "rb")
authors = pickle.load(authors_file_handler)
authors_file_handler.close()

words_file_handler = open(words_file, "rb")
word_data = pickle.load(words_file_handler)
words_file_handler.close()

### test_size is the percentage of events assigned to the test set. remainder go into training

features_train, features_test, labels_train, labels_test =\
     cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

### text vectorization--go from strings to lists of numbers
     
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words= 'english')
features_train_transformed = vectorizer.fit_transform(features_train)
features_test_transformed  = vectorizer.transform(features_test)

### feature selection, because text is super high dimensional and 
### can be really computationally chewy as a result, selector = SelectPercentile(f_classif, percentile=10)

selector = SelectPercentile(f_classif, percentile = 1)
selector.fit(features_train_transformed, labels_train)
features_train_transformed = selector.transform(features_train_transformed).toarray()
features_test_transformed  = selector.transform(features_test_transformed).toarray()

### Print info on the data

print ("no. of Chris training emails:", sum(labels_train))
print ("no. of Sara training emails:", len(labels_train)-sum(labels_train))

# Classify the emails

from sklearn import tree

def classify(features_train, labels_train):
       
    ### should return a trained decision tree classifer
    clf = tree.DecisionTreeClassifier(min_samples_split=40)
    clf = clf.fit(features_train, labels_train)
    
    return clf

clf = classify(features_train_transformed, labels_train)

#### store predictions in a list named pred

pred = clf.predict(features_test_transformed)


from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print("accuracy Score is: ", acc)

#########################################################


