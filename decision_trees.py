#%%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier

from utilities import visualize_classifier
#%%
# Load input data
input_file = 'data_decision_trees.txt'

data = np.loadtxt(input_file, delimiter=',')
X, y = data[:, :-1], data[:, -1]

X[1:5]
y[1:5]
data.shape
np.mean(X, axis = 0)
#%%
# Separate input data into two classes based on labels
class_0 = np.array(X[y==0])
class_1 = np.array(X[y==1])

# Visualize input data
plt.figure()
plt.scatter(class_0[:, 0], class_0[:, 1], s=75, facecolors='brown', 
        edgecolors='orange', linewidth=1, marker='x')

plt.scatter(class_1[:, 0], class_1[:, 1], s=75, facecolors='white', 
        edgecolors='orange', linewidth=1, marker='o')
plt.title('Input Data')
plt.show()
#%%
"""
Entropy (a way to measure impurity) - entropy 0 if node belongs to the same class (prob = 1, log(1) = 0)
Gini index (a criterion to minimize the probability of misclassification)
Classification Error (miscllaification error)
"""
# Split data into training and testing datasets 
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
        X, y, test_size=0.25, random_state=5)

# Decision Trees classifier 
params = {'random_state': 0, 'max_depth': 4, 'criterion': "gini"}
classifier = DecisionTreeClassifier(**params)
classifier.fit(X_train, y_train)
visualize_classifier(classifier, X_train, y_train, 'Training dataset')

y_test_pred = classifier.predict(X_test)
visualize_classifier(classifier, X_test, y_test, 'Test dataset')
#%%
"""
The performance of a classifier is characterized by precision, recall, and f1-scores.
Precision refers to the accuracy of the classification and recall refers to the number of items
that were retrieved as a percentage of the overall number of items that were supposed to be
retrieved. A good classifier will have high precision and high recall, but it is usually a tradeoff
between the two. Hence we have f1-score to characterize that. F1 score is the harmonic
mean of precision and recall, which gives it a good balance between precision and recall
values.
"""
# Evaluate classifier performance
class_names = ['Class-0', 'Class-1']
print("\n" + "#"*40)
print("\nClassifier performance on training dataset\n")
print(classification_report(y_train, classifier.predict(X_train), target_names=class_names))
print("#"*40 + "\n")

print("#"*40)
print("\nClassifier performance on test dataset\n")
print(classification_report(y_test, y_test_pred, target_names=class_names))
print("#"*40 + "\n")

#%
## confusion Matrix
from sklearn.metrics import confusion_matrix

confusion_matrix = confusion_matrix(y_test, y_test_pred)
print("confusion Matrix:\n", confusion_matrix)
#%%
# Visualize tree
from sklearn import tree

with open("my_tree.txt", "w") as f:
    f = tree.export_graphviz(classifier, out_file=f)

## Code has been generated in the same directory. Copy and paste on http://www.webgraphviz.com/
#%%    
## importances
importances = classifier.feature_importances_

indices = np.argsort(importances) [::-1]

print ('Feature Ranking: ')
for i in range(2):
    print ("{} feature no.{} ({})".format(i+1,indices[i],importances[indices[i]]))
#%%