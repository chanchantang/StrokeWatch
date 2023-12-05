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
from joblib import dump


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
clf2 = LogisticRegression(max_iter=10000)
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

           0       0.95      0.81      0.87       940
           1       0.00      0.00      0.00        42

    accuracy                           0.77       982
   macro avg       0.47      0.40      0.44       982
weighted avg       0.91      0.77      0.84       982

Voting Classifier with Soft Voting Classification Report:

              precision    recall  f1-score   support

           0       0.95      0.78      0.85       940
           1       0.00      0.00      0.00        42

    accuracy                           0.75       982
   macro avg       0.47      0.39      0.43       982
weighted avg       0.91      0.75      0.82       982

'''


# accuracy scores
score_hard = accuracy_score(y_test, y_pred_hard)
score_soft = accuracy_score(y_test, y_pred_soft)
#print("Hard Voting Accuracy Score % d" % score_hard)
#print("Soft Voting Accuracy Score % d" % score_soft)

'''
Hard and Soft Voting Scores from above print statements:
Hard Voting Score  0
Soft Voting Score  0
'''


# confusion matrices
CM_hard = confusion_matrix(y_test, y_pred_hard)
CM_soft = confusion_matrix(y_test, y_pred_soft)
#print('Confusion Matrix for Hard Voting is : \n', CM_hard)
#print('Confusion Matrix for Soft Voting is : \n', CM_soft)

'''
Confusion Matrix for Hard Voting is : 
 [[760 180]
 [ 42   0]]
Confusion Matrix for Soft Voting is : 
 [[732 208]
 [ 42   0]]
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
[0.9317819148936171, 0.8861702127659574, 0.8606382978723406, 0.9339095744680851]
'''

# Save model
dump(eclf1, '../saved_models/' + 'voting_classifier_hard' + '.joblib')
dump(eclf2, '../saved_models/' + 'voting_classifier_soft' + '.joblib')
