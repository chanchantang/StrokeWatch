# Stroke prediction using LOGISTIC REGRESSION model
# Reference: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from joblib import dump

train_data_path = '../raw_data/train_data.csv'
test_data_path = '../raw_data/test_data.csv'

train_data = pd.read_csv(train_data_path)
test_data = pd.read_csv(test_data_path)

X_train = train_data.drop('stroke', axis = 1)
y_train = train_data['stroke']

X_test = test_data.drop('stroke', axis = 1)
y_test = test_data['stroke']


## Logistic Regression Model ##
# See reference link, line 2
# Parameters left as default: penalty, solver
# Parameters changed:
# --> tol (tolerance) - smaller than default, which can help allow optimization process to continue until small changes observed
# --> C (regularization strength) - choosing smaller than default can help prevent overfitting, which can be a problem after using SMOTE
# --> class_weight - 'balanced' helps in dealing with imbalanced classes
# --> max_iter - using default of 100 resulted in the model failing to converge, but increase to 200 solved the issue

log_reg_model = LogisticRegression(
    penalty = 'l2',
    tol = 1e-5,
    C = 0.1,
    class_weight = 'balanced',
    solver = 'lbfgs',
    max_iter = 2000   
)

# fitting the data
log_reg_model.fit(X_train, y_train)

# predictions on the data
y_prediction = log_reg_model.predict(X_test)


## Model Evaluation ##
log_reg_accuracy = accuracy_score(y_test, y_prediction)
log_reg_confusion_matrix = confusion_matrix(y_test, y_prediction)
log_reg_classification_report = classification_report(y_test, y_prediction)

print(f'Accuracy: {round(log_reg_accuracy*100, ndigits = 2)}%')
print('Classification Report:\n', log_reg_classification_report)
print('Confusion Matrix:\n', log_reg_confusion_matrix)

""" Results of the above print statements:
Accuracy:  93.99%
Classification Report:
               precision    recall  f1-score   support

           0       0.96      0.97      0.97       940
           1       0.23      0.17      0.19        42

    accuracy                           0.94       982
   macro avg       0.59      0.57      0.58       982
weighted avg       0.93      0.94      0.94       982

Confusion Matrix:
 [[916  24]
 [ 35   7]]
"""
# Save model
#dump(log_reg_model, '../../saved_models/' + 'logistic_regression' + '.joblib')