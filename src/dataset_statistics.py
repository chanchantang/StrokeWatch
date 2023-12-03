#!/usr/bin/env python
# coding: utf-8

# ## Load data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from sklearn.preprocessing import LabelEncoder

def load_dataset(dataset_path):
    df = pd.read_csv(dataset_path)
    features = df.drop(columns=['stroke'])
    labels= df['stroke']
    return features, labels, df

dataset_path = "./../raw_data/raw_data.csv"

features, labels, df = load_dataset(dataset_path)
df = df.dropna()


# ## Extract dataset information

# ### Show dataset
df.head()


# ### Descriptive statistics
data_types = {
    'categorical': ['gender', 'work_type', 'Residence_type', 'smoking_status'],
    'boolean': ['hypertension''heart_disease', 'ever_married', 'stroke'],
    'numerical' : ['age', 'avg_glucose_level', 'bmi']
}

df.describe(include='all')


# ### Unique values for each column
print("Unique Count")
for column in df.columns:
    num_unique = len(df[column].unique())
    print(f'{column}: {num_unique}')


# ### Plot frequency for categorical and numerical columns
# Plot for categorical/boolean columns: gender, hypertension, heart_disease, ever_married, work_type, Residence_type, smoking_status, stroke
def plot_counts_categorical(column_name):
    if len(df[column_name].unique()) > 5:
        print("Column is not categorical, please use a categorical column")
        return
    df[column_name].value_counts().plot(kind='bar')
    plt.title(f'{column_name} count')
    plt.ylabel("number of individuals")
    plt.show()

for column in df.columns:
    if column in data_types['categorical'] or column in data_types['boolean']:
        plot_counts_categorical(column)

# Histogram for numerical columns: age, avg_glucose_level, bmi
def plot_counts_numerical(column_name, step = 10):
    if column_name not in data_types['numerical']:
        print("Column is not numerical, please use a numerical column")
        return

    min = math.floor(features[column_name].min())
    max = math.ceil(features[column_name].max())
    bins = np.arange(start=min + step, stop=max, step = step)

    plt.hist(features[column_name], bins=bins, edgecolor='black')
    plt.title(f"{column_name} count")
    plt.ylabel("number of individuals")
    plt.xlabel(f"{column_name}")
    plt.show()
    
plot_counts_numerical('age', 5)
plot_counts_numerical('avg_glucose_level', 20)
plot_counts_numerical('bmi', 5)


# ### Distribution of stroke
# Comparing the makeup percentage of categorical or boolean variables to stroke 
def distribution_comparison(column_name):
    if df[column_name].dtype != float and df[column_name].dtype != int:
        pass
    sns.catplot(data=df, y='stroke', x=column_name, kind='bar')
    plt.title(f"Distribution of {column_name} with stroke")
    plt.show()

for column in df.columns:
    if column in data_types['categorical'] or column in data_types['boolean']:
        if column == 'stroke':
            continue
        distribution_comparison(column)

# Show distribution of continous columns with those with strike and those without
def distribution_num(column_name, bins = 10):
    with_stroke = df[df['stroke'] == 1]
    no_stroke = df[df['stroke'] == 0]

    # With stroke
    plt.figure(1)
    plt.hist(with_stroke[column_name], color='red', bins=bins, edgecolor='black')
    plt.title(f"Distribution of {column_name} against stroke")
    plt.legend(['with stroke'])
    plt.xlabel(f"{column_name}")
    plt.ylabel("number of individuals")

    # Without stroke
    plt.figure(2)
    plt.hist(no_stroke[column_name], color='blue', bins=bins, edgecolor='black')
    plt.title(f"Distribution of {column_name} against stroke")
    plt.legend(['no stroke'])
    plt.xlabel(f"{column_name}")
    plt.ylabel("number of individuals")
    plt.show()
    
distribution_num('avg_glucose_level')



# ### Encoding with labeling
def label_encoding(df):
    le = LabelEncoder()
    df['gender'] = le.fit_transform(df['gender'])
    df['ever_married'] = le.fit_transform(df['ever_married'])
    df['work_type'] = le.fit_transform(df['work_type'])
    df['Residence_type'] = le.fit_transform(df['Residence_type'])
    df['smoking_status'] = le.fit_transform(df['smoking_status'])
    return df

df = label_encoding(df)


# ### Values after labeling
for column in df.columns:
    if column in data_types['categorical']:
        print(f'{column}: {df[column].unique()}')


# ### Correlation matrix 
def correlation_matrix(threshold_status, threshold = 0):
    corr_matrix = df.corr()
    if not threshold_status: 
        plt.figure(figsize=(10, 10))
        sns.heatmap(corr_matrix, annot=True)
        plt.show()
    else:
        plt.figure(figsize=(10, 10))
        matrix_with_threshold = corr_matrix.abs() > threshold
        sns.heatmap(matrix_with_threshold)

correlation_matrix(False)
correlation_matrix(True, 0.3)

