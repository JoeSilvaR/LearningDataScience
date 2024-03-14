# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:42:59 2024

@author: josep
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import scipy as sp




filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(filepath, header=0)


## Linear Regression
from sklearn.linear_model import LinearRegression

lm = LinearRegression()

x= df[['engine-size']]
y= df['price']

lm.fit(x,y)

Yhat = lm.predict(x)
Yhat[0:5]
lm.intercept_
lm.coef_

Yhat_eq=-7963.3 +166.86*y

##Mutliple Linear Regression
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
y= df['price']

lm.fit(Z,y)

lm.intercept_
lm.coef_

Yhat_mlr_eq = -15806.62 +53.496*y +4.71*y+ 81.53*y + 36.06*y

## Model Evaluation usin Viz's

import seaborn as sns

# Linear plot
height = 10
width = 12
x= df['highway-mpg']
y= df['price']
plt.figure(figsize= (width, height))

sns.regplot(x=x, y=y, data=df)
plt.ylim(0,)

plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)

# verifying correlations
df[['peak-rpm', 'price']].corr()
df[['highway-mpg', 'price']].corr()

# residual plot
height = 10
width = 12
x= df['highway-mpg']
y= df['price']
plt.figure(figsize = (width,height))
sns.residplot(x=x, y=y)
plt.ylim(0,)

# Multiple Linear Regression

Y_hat = lm.predict(Z)

plt.figure(figsize=(width, height))

ax1  = sns.distplot(df['price'], hist =False, color='r', label ='Actual Values')
sns.distplot(Y_hat, hist = False, color= 'b', label ='Fitted Values', ax = ax1)

plt.title('Actual Vs. Fitted Vales for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Propotion of Cars')

## Polynomial Regression and Pipelines

def PlotPolly(model, independent_variable, dependant_variable, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependant_variable, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

x= df[['highway-mpg']]
y= df['price']

f= np.polyfit(x, y, 11)
p =np.poly1d(f)
print(p)

PlotPolly(p, x,y , 'highway-mpg')
np.polyfit(x, y, 3)


#Polynomial transform
from sklearn.preprocessing import PolynomialFeatures

pr = PolynomialFeatures(degree=2)
Z_pr = pr.fit_transform(Z)

#Pipelines

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(include_bias = False)),
         ('model', LinearRegression())]

pipe = Pipeline(Input)

Z = Z.astype(float)
pipe.fit(Z,y)

ypipe = pipe.predict(Z)


## Measures for In Sample Evaluation

# R^2 and MSE with simple linear regression
# highway-mpg fit
from sklearn.metrics import mean_squared_error
lm.fit(x,y)
lm.score(x,y)

Yhat = lm.predict(x)
mse= mean_squared_error(y,Yhat)
mse

#MLR error checking
lm.fit(Z, y)
lm.score(Z, y)

Yhat_multi = lm.predict(Z)
mse_multi = mean_squared_error(y, Yhat_multi)
mse_multi

#polynomial fit
from sklearn.metrics import r2_score

r_squared = r2_score(y, p(x))
r_squared

mean_squared_error(y, p(x))
