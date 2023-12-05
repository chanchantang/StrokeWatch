import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn. metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from joblib import dump, load

# Import preprocessed data
train_data_path = '../raw_data/train_data.csv'
test_data_path = '../raw_data/test_data.csv'
train_data = pd.read_csv(train_data_path)
test_data  = pd.read_csv(test_data_path)

# Split into train and test sets
X_train = train_data.drop('stroke', axis=1)
y_train = train_data['stroke']
X_test = test_data.drop('stroke', axis=1)
y_test = test_data['stroke']

{
# Train model using parameters optimized from gridsearch
# model = RandomForestClassifier(random_state=340)
# parameters = {
#    'n_estimators':[100,110,120,130,140,150],
#    'criterion':['gini', 'entropy', 'log_loss'],
#    'min_samples_split':[1,2,5,7,10],
#    'min_samples_leaf':[1,2,5,10,20],
#    'random_state': [340,24]

# }
# grid = GridSearchCV(model, param_grid=parameters, cv=10, n_jobs=-1, verbose=1)
# grid.fit(X_train, y_train)
# print(grid.best_score_)
# print(grid.best_params_)
}

model = RandomForestClassifier(n_estimators=100, criterion='gini', min_samples_leaf=1, min_samples_split=2, random_state=16)
model.fit(X_train, y_train)
#print(model.score(X_train, y_train))
#print(model.score(X_test, y_test))

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print the results
#print(f'Accuracy: {round(accuracy*100, ndigits = 2)}%')
#print(f'Confusion Matrix:\n{conf_matrix}')
#print(f'Classification Report:\n{class_report}')

""" Results of the above print statements:
Accuracy: 90.73%
Confusion Matrix:
[[881  59]
 [ 32  10]]
Classification Report:
              precision    recall  f1-score   support

           0       0.96      0.94      0.95       940
           1       0.14      0.24      0.18        42

    accuracy                           0.91       982
   macro avg       0.55      0.59      0.57       982
weighted avg       0.93      0.91      0.92       982
"""

#### Use in .ipynb for stats below to extract graphs ###

# Plot confusion matrix
# cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
# cm_display.plot()
# plt.show()

# Visualize decision tree (may need to put in ipynb to extract graph)
# plt.figure(figsize = (80, 20))
# plot_tree(clf, feature_names=X_train.columns, class_names={0:'Negative', 1:'Stroke'},  max_depth=3, filled=True)

# To save/load model 
dump(model, '../saved_models/' + 'random_forest' + '.joblib')