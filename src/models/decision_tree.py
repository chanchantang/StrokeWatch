import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import GridSearchCV
from sklearn. metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from joblib import dump, load

# Import preprocessed data
train_data_path = '../../raw_data/train_data.csv'
test_data_path = '../../raw_data/test_data.csv'
train_data = pd.read_csv(train_data_path)
test_data  = pd.read_csv(test_data_path)

# Unnamed column in prepocessed data? Removing for now
# train_data = train_data.drop(columns=train_data.columns[0], axis=1)
# test_data = test_data.drop(columns=test_data.columns[0], axis=1)

# Split into train and test sets
X_train = train_data.drop('stroke', axis = 1)
y_train = train_data['stroke']
X_test = test_data.drop('stroke', axis = 1)
y_test = test_data['stroke']

# Train model using parameters optimized from gridsearch
clf = DecisionTreeClassifier(ccp_alpha=0, criterion="entropy", max_depth=18, min_samples_leaf=2, random_state=42)
clf.fit(X_train, y_train)
y_prediction = clf.predict(X_test)

# Accuracy statistics
accuracy = accuracy_score(y_test, y_prediction)
report = classification_report(y_test, y_prediction)
cm = confusion_matrix(y_test, y_prediction)
parameters = clf.get_params()
feature_importance = pd.DataFrame(clf.feature_importances_, index = X_train.columns)

# Print the results
print(f'Accuracy: {round(accuracy*100, ndigits = 2)}%')
print(f'Confusion Matrix:\n{cm}')
print(f'Classification Report:\n{report}')

""" Results of the above print statements:
Accuracy: 91.45%
Confusion Matrix:
[[893  47]
 [ 37   5]]
Classification Report:
              precision    recall  f1-score   support

           0       0.96      0.95      0.96       940
           1       0.10      0.12      0.11        42

    accuracy                           0.91       982
   macro avg       0.53      0.53      0.53       982
weighted avg       0.92      0.91      0.92       982
"""


# Use gridsearch to tune hyperparameters
'''
parameters = {
    'criterion':['gini', 'entropy'],
    'max_depth':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    'ccp_alpha':[0, 0.01, 0.1],
    'min_samples_leaf':[1, 2, 3],
}
grid = GridSearchCV(clf, param_grid=parameters, cv=10, n_jobs = -1, verbose=1)

grid.fit(X_train, y_train)

print(grid.best_score_)
print(grid.best_params_)
'''

# To save/load model 
# dump(clf, '../../saved_models/' + 'decision_tree' + '.joblib')
# loaded_clf = load('../saved_models/' + 'decision_tree.' + 'joblib')

#### Use in .ipynb for stats below to extract graphs ###

# Plot confusion matrix
# cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
# cm_display.plot()
# plt.show()

# Visualize decision tree (may need to put in ipynb to extract graph)
# plt.figure(figsize = (80, 20))
# plot_tree(clf, feature_names=X_train.columns, class_names={0:'Negative', 1:'Stroke'},  max_depth=3, filled=True)

# To save/load model 
# dump(clf, '../saved_models/' + 'decision_tree' + '.joblib')
# loaded_clf = load('../saved_models/' + 'decision_tree.' + 'joblib')