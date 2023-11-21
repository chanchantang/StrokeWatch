import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the datasets
train_data_path = '../raw_data/train_data.csv'
test_data_path = '../raw_data/test_data.csv'

train_data = pd.read_csv(train_data_path)
test_data = pd.read_csv(test_data_path)

X_train = train_data.drop('stroke', axis=1)
y_train = train_data['stroke']

X_test = test_data.drop('stroke', axis=1)
y_test = test_data['stroke']

# Create and train the Naive Bayes model
naive_bayes_model = GaussianNB()
naive_bayes_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = naive_bayes_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print the results
print(f'Accuracy: {round(accuracy*100, ndigits = 2)}%')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
