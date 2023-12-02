import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import MultinomialNB
from joblib import dump
# Load the datasets
train_data_path = '../raw_data/train_data.csv'
test_data_path = '../raw_data/test_data.csv'

train_data = pd.read_csv(train_data_path)
test_data = pd.read_csv(test_data_path)

x_train = train_data.drop('stroke', axis=1)
y_train = train_data['stroke']

x_test = test_data.drop('stroke', axis=1)
y_test = test_data['stroke']

# Create and train the Naive Bayes model
naive_bayes_model = MultinomialNB(alpha=1)
naive_bayes_model.fit(x_train, y_train)

# Make predictions on the test set
y_pred = naive_bayes_model.predict(x_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print the results
print(f'Accuracy: {round(accuracy*100, ndigits = 2)}%')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')

""" Results of the above print statements:
Accuracy: 73.42%
Confusion Matrix:
[[693 247]
 [ 14  28]]
Classification Report:
              precision    recall  f1-score   support

           0       0.98      0.74      0.84       940
           1       0.10      0.67      0.18        42

    accuracy                           0.73       982
   macro avg       0.54      0.70      0.51       982
weighted avg       0.94      0.73      0.81       982

"""
# Export model
#dump(naive_bayes_model, '../../saved_models/' + 'naive_bayes' + '.joblib')