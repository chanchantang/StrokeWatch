#!/usr/bin/env python
# coding: utf-8

from joblib import load
import pandas as pd 
from sklearn. metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load models
SAVED_MODELS_PATH = '../saved_models/'

decision_tree = load(SAVED_MODELS_PATH+ 'decision_tree.' + 'joblib')
logistic_regression = load(SAVED_MODELS_PATH+ 'logistic_regression.' + 'joblib')
naive_bayes = load(SAVED_MODELS_PATH+ 'naive_bayes.' + 'joblib')
random_forest = load(SAVED_MODELS_PATH+ 'random_forest.' + 'joblib')
voting_classifier_hard = load(SAVED_MODELS_PATH+ 'voting_classifier_hard.' + 'joblib')
voting_classifier_soft = load(SAVED_MODELS_PATH+ 'voting_classifier_soft.' + 'joblib')

model_names = ['decision tree', 'logistic regression', 'naive bayes', 'random forest', 'voting classifier hard', 'voting classifier soft']

# Load data
train_data_path = '../raw_data/train_data.csv'
test_data_path = '../raw_data/test_data.csv'
train_data = pd.read_csv(train_data_path)
test_data  = pd.read_csv(test_data_path)

# Split into train and test sets
X_train = train_data.drop('stroke', axis=1)
y_train = train_data['stroke']
X_test = test_data.drop('stroke', axis=1)
y_test = test_data['stroke']

models = [decision_tree, logistic_regression, naive_bayes, random_forest, voting_classifier_hard, voting_classifier_soft]

# Overall accuracy
i = 0
print('Accuracy\n--------')
for model in models:
    y_pred = model.predict(X_test)
    print(f'{model_names[i]} {accuracy_score(y_test, y_pred)}')
    i += 1

# Classification report
i = 0
print('Classification report\n--------')
for model in models:
    y_pred = model.predict(X_test)
    print(f'{model_names[i]}\n {classification_report(y_test, y_pred)}')
    i += 1

# Confusion matrix
i = 0
print('\nConfusion Matrix\n--------')
for model in models:
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    cm_display.plot()
    plt.title(model_names[i])
    plt.show()
    i += 1

# TPR and TNR 
i = 0
print('\nPositive and negative rates\n--------')
for model in models:
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    TP = cm[1][1]
    TN = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]
    print(model_names[i])
    print(f"TPR rate: {round(TP/(TP + FN), 2) * 100}%")
    print(f"TNR rate: {round(TN/(TN + FP), 2) * 100}%\n")
    i += 1