# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the dataset
car_data=pd.read_csv('/Users/KIIT/Downloads/car data.csv')

car_data.head()

car_data

# Data cleaning
car_data.info()

car_data.isnull().sum()

car_data['Fuel_Type'].value_counts()
car_data['Seller_Type'].value_counts()
car_data['Transmission'].value_counts()

# Encoding the data
# 0-Petrol 1-Diesel 2-CNG
car_data.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)


# 0-Dealer 1-Individual
car_data.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)

# 0-Manual 1-Automatic
car_data.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)

car_data

car_data.info()

# Applying Machine learning algorithms
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn import metrics

car_data.info()

X=car_data.drop(['Car_Name','Selling_Price'],axis=1)
Y=car_data['Selling_Price']

X

Y

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,random_state=2)

lin_reg_model=LinearRegression()

lin_reg_model.fit(X_train,Y_train)

prediction=lin_reg_model.predict(X_train)

error_score=metrics.r2_score(Y_train,prediction)
print("Squared Error: ",error_score)

# Data Visualisation using graphs
plt.scatter(Y_train,prediction)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual Prices vs Predicted Prices')
plt.show()

test_data_prediction=lin_reg_model.predict(X_test)

# Calculating error score
error_score=metrics.r2_score(Y_test,test_data_prediction)
print("Squared Error: ",error_score)

plt.scatter(Y_test,test_data_prediction)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual Prices vs Predicted Prices')
plt.show()

las_reg_model=Lasso()

las_reg_model.fit(X_train,Y_train)

prediction=las_reg_model.predict(X_train)

error_score=metrics.r2_score(Y_train,prediction)
print("Squared Error: ",error_score)

plt.scatter(Y_train,prediction)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual Prices vs Predicted Prices')
plt.show()

test_data_prediction=las_reg_model.predict(X_test)

error_score=metrics.r2_score(Y_test,test_data_prediction)
print("Squared Error: ",error_score)

plt.scatter(Y_test,test_data_prediction)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual Prices vs Predicted Prices')
plt.show()

from xgboost import XGBRegressor

xgb_reg_model=XGBRegressor()
xgb_reg_model.fit(X_train,Y_train)

error_score=metrics.r2_score(Y_train,prediction)
print("Squared Error: ",error_score)

plt.scatter(Y_train,prediction)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual Prices vs Predicted Prices')
plt.show()

test_data_prediction=xgb_reg_model.predict(X_test)

error_score=metrics.r2_score(Y_test,test_data_prediction)
print("Squared Error: ",error_score)

plt.scatter(Y_test,test_data_prediction)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual Prices vs Predicted Prices')
plt.show()

