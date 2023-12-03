#!/usr/bin/env python
# coding: utf-8
import pandas as pd

INPUT_DATA_DIR = "./../raw_data_old/"

df = pd.read_csv("./../raw_data/" + "raw_data.csv")

# Check for null values in each column
null_counts = df.isnull().sum()

# Print the null counts for each column
#print(null_counts)

# Drop rows with any null values
df_cleaned = df.dropna()

# Drop id column
df_cleaned = df_cleaned.drop(['id'], axis=1)

# Encoding categorical variables
df_cleaned = pd.get_dummies(df_cleaned, columns=['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])

df_cleaned.to_csv(INPUT_DATA_DIR + 'cleaned_data.csv', index=False)

from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

# Split the data and result
X = df_cleaned[df_cleaned.columns.difference(['stroke'])]
y = df_cleaned['stroke']
#df_cleaned.shape

# Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=340)
print('Ratio of nonstrokes/strokes in training data: {}'.format(sum(y_train == 0)/sum(y_train == 1)))
print('Ratio of nonstrokes/strokes in testing data: {} \n'.format(sum(y_test == 0)/sum(y_test == 1)))

print("Before OverSampling, counts of label '1': {}".format(sum(y_train == 1))) 
print("Before OverSampling, counts of label '0': {} \n".format(sum(y_train == 0)))

# Use SMOTE to create stroke samples from the training data
sm = SMOTE(k_neighbors=5)

X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

print("After OverSampling, counts of label '1': {}".format(sum(y_train_res == 1)))
print("After OverSampling, counts of label '0': {}".format(sum(y_train_res == 0)))

# Create new file with new training data
train_data = X_train_res
train_data['stroke'] = y_train_res

# Create new file with testing data
test_data = X_test
test_data['stroke'] = y_test

train_data.to_csv(INPUT_DATA_DIR + 'train_data.csv', index=False)
test_data.to_csv(INPUT_DATA_DIR + 'test_data.csv', index=False)