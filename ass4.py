# -*- coding: utf-8 -*-
"""ass4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HUTdLfycxcKIB3qIqhxaH-mpAf1gfHvn
"""

# import the required libraries.
import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

from google.colab import files
uploaded= files.upload()

import io
df_boston= pd.read_csv(io.BytesIO(uploaded['HousingData.csv']))

#load the housing data from scikit-learn library and understand it
from sklearn.datasets import load_boston
boston_dataset= load_boston

print(df.describe())

df_boston.head()

print(df_boston.isnull().sum())

type(boston_dataset().keys())

print(boston_dataset().DESCR)

df_boston = pd.DataFrame(boston_dataset().data, columns=boston_dataset().feature_names)

df_boston['MEDV']= boston_dataset().target

df_boston.head()

sbn.set(rc={'figure.figsize':(11.7,8.27)})
sbn.distplot(df_boston['MEDV'],bins=30)
plt.show()

correlation_matrix= df_boston.corr().round(2)
sbn.set(rc={'figure.figsize':(11.7,8.27)})
sbn.heatmap(data=correlation_matrix,annot=True)
plt.show()

plt.figure(figsize=(20,5))

features=['LSTAT', 'RM']
target=df_boston['MEDV']

for i,col in enumerate(features):
  plt.subplot(1, len(features), i+1)
  x=df_boston[col]
  y= target
  plt.scatter(x,y, marker='o')
  plt.title(col)
  plt.xlabel(col)
  plt.ylabel('MEDV')

plt.show()

#concatenate the 'LSTAT' and 'RM' column usng np.c_ from pandas library 
x=pd.DataFrame(np.c_[ df_boston['LSTAT'], df_boston['RM']], columns=['LSTAT', 'RM'])
y = df_boston['MEDV']

from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test =train_test_split(x, y, test_size=0.2, random_state=5)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lin_model = LinearRegression()
lin_model.fit(x_train, y_train)

from sklearn.metrics import r2_score

y_train_predict = lin_model.predict(x_train)
rmse = (np.sqrt(mean_squared_error(y_train,y_train_predict )))
r2= r2_score(y_train, y_train_predict)
print("The model performance for training set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")


#RMSE (Root Mean Square Error) tells how concentrated the data is around the line of best fit

y_test_predict = lin_model.predict(x_test)
rmse = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2 = r2_score(y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

