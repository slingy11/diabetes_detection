# -*- coding: utf-8 -*-
"""Major Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13_f65XrcgPGmD5A3kEEwRj2npuwlI7xj
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')
df.head()

df.isnull().values.any()

df.describe

df.isnull().sum()

df.corr()

corr = df.corr()
fig, ax = plt.subplots(figsize=(20,18))
sns.heatmap(corr, annot=True, ax=ax, cmap = 'coolwarm')

from sklearn.model_selection import train_test_split
X = df.drop(columns=['Outcome'])
Y = df['Outcome']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.40)

# logistic regression 
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(x_train, y_train)

print("Accuracy: ",model.score(x_test, y_test) * 100)

# decision tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

model.fit(x_train, y_train)

print("Accuracy: ",model.score(x_test, y_test) * 100)

# knn - k-nearest neighbours
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()

model.fit(x_train, y_train)

print("Accuracy: ",model.score(x_test, y_test) * 100)

