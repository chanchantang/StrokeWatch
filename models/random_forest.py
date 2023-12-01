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

# Train model using parameters optimized from gridsearch
# model = RandomForestClassifier()
# parameters = {
#     'n_estimators':[100,110,120,130,140,150],
#     'criterion':['gini', 'entropy', 'log_loss'],
#     'min_samples_split':[1,2,5,7,10],
#     'min_samples_leaf':[1,2,5,10,20]
# }
# grid = GridSearchCV(model, param_grid=parameters, cv=10, n_jobs=-1, verbose=1)
# grid.fit(X_train, y_train)
# print(grid.best_score_)
# print(grid.best_params_)

model = RandomForestClassifier(n_estimators=100, criterion='entropy', min_samples_leaf=1, min_samples_split=5)
model.fit(X_train, y_train)
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

# model = RandomForestClassifier(n_estimators=140, criterion='gini', min_samples_leaf=1, min_samples_split=5)
# model.fit(X_train, y_train)
# print(model.score(X_train, y_train))
# print(model.score(X_test, y_test))

# y_prediction = model.predict(X_test)
# # Accuracy statistics
# accuracy = accuracy_score(y_test, y_prediction)
# report = classification_report(y_test, y_prediction)
# cm = confusion_matrix(y_test, y_prediction)
# parameters = model.get_params()
# feature_importance = pd.DataFrame(model.feature_importances_, index=X_train.columns)
# print(accuracy)






# To save/load model 
# dump(clf, '../saved_models/' + 'decision_tree' + '.joblib')
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