# CMPT 340 - Voting Classifier model for stroke prediction
# November 12, 2023

# References: 
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html
# https://towardsdatascience.com/custom-implementation-of-feature-importance-for-your-voting-classifier-model-859b573ce0e0
# https://www.youtube.com/watch?v=LXc6LpFWCEQ
# https://www.kaggle.com/code/saurabhshahane/voting-classifier#
# https://www.kaggle.com/code/zayanmakar/voting-classifier-for-prediction

import pandas as pd
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score


# import pre-processed data
train_data_path = "../raw_data/train_data.csv"
test_data_path  = "../raw_data/test_data.csv"
train_data = pd.read_csv(train_data_path)
test_data  = pd.read_csv(test_data_path)


# training and testing sets
X_train = train_data.drop('stroke', axis = 1)   # features
y_train = train_data['stroke']                  # outcomes

X_test = test_data.drop('stroke', axis = 1)
y_test = test_data['stroke']


# classifiers for Voting Classifier
clf1 = RandomForestClassifier()
clf2 = LogisticRegression(max_iter=1000)
clf3 = DecisionTreeClassifier()
clf4 = GaussianNB()

estimators = [('RandomForest', clf1), ('LogisticRegression', clf2), ('DecisionTree', clf3), ('NaiveBayes', clf4)]


# Voting Classifier with Hard Voting
eclf1 = VotingClassifier(estimators=estimators, voting='hard')
eclf1.fit(X_train, y_train)
y_pred_hard = eclf1.predict(X_test)


# Voting Classifier with Soft Voting
eclf2 = VotingClassifier(estimators=estimators, voting='soft')
eclf2.fit(X_train, y_train)
y_pred_soft = eclf2.predict(X_test)




####### Model Evaluation #######

# Classification Reports
# print(classification_report(y_test, y_pred_hard))
# print(classification_report(y_test, y_pred_soft))

'''
Voting Classifier with Hard Voting Classification Report:

              precision    recall  f1-score   support

           0       0.95      0.79      0.86       941
           1       0.00      0.00      0.00        41

    accuracy                           0.75       982
   macro avg       0.47      0.39      0.43       982
weighted avg       0.91      0.75      0.82       982

Voting Classifier with Soft Voting Classification Report:

              precision    recall  f1-score   support

           0       0.94      0.75      0.84       941
           1       0.00      0.00      0.00        41

    accuracy                           0.72       982
   macro avg       0.47      0.37      0.42       982
weighted avg       0.91      0.72      0.80       982

'''


# accuracy scores
score_hard = accuracy_score(y_test, y_pred_hard)
score_soft = accuracy_score(y_test, y_pred_soft)
# print("Hard Voting Accuracy Score % d" % score_hard)
# print("Soft Voting Accuracy Score % d" % score_soft)

'''
Hard and Soft Voting Scores from above print statements:
Hard Voting Score  0
Soft Voting Score  0
'''


# confusion matrices
CM_hard = confusion_matrix(y_test, y_pred_hard)
CM_soft = confusion_matrix(y_test, y_pred_soft)
# print('Confusion Matrix for Hard Voting is : \n', CM_hard)
# print('Confusion Matrix for Soft Voting is : \n', CM_soft)

'''
Confusion Matrix for Hard Voting is : 
 [[759 182]
 [ 41   0]]
Confusion Matrix for Soft Voting is : 
 [[699 242]
 [ 41   0]]
'''

# cross val scores
c = []
c.append(cross_val_score(clf1, X_train, y_train, scoring='accuracy', cv=10).mean())
c.append(cross_val_score(clf2, X_train, y_train, scoring='accuracy', cv=10).mean())
c.append(cross_val_score(clf3, X_train, y_train, scoring='accuracy', cv=10).mean())
c.append(cross_val_score(clf4, X_train, y_train, scoring='accuracy', cv=10).mean())
# print(c)


'''
Cross val scores from above print statement:
[0.92721212142675, 0.9047380088959402, 0.8371614443153808, 0.9318722200186984]
'''