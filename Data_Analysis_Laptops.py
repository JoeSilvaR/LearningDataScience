# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 09:52:48 2024

@author: josep
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

filepath="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(filepath, header=0)

#Creating Regression plots "CPU_frequency", "Screen_Size_inch" and "Weight_pounds" against "Price"
fig, axes = plt.subplots(nrows =3, ncols=1, figsize = (8,12))

sns.regplot(x=df['CPU_frequency'], y ='Price', data = df, ax =axes[0])
axes[0].set_ylim(0,)

sns.regplot(x = 'Screen_Size_inch', y= 'Price', data = df, ax=axes[1])
axes[1].set_ylim(0,)

sns.regplot(x = 'Weight_pounds', y= 'Price', data = df, ax=axes[2])
axes[2].set_ylim(0,)

plt.tight_layout()
plt.show()

#Correlation
df[['CPU_frequency','Screen_Size_inch','Weight_pounds', 'Price']].corr()

#Boxplot categorical variables Category", "GPU", "OS", "CPU_core", "RAM_GB", "Storage_GB_SSD"
fig_2,axes_2 = plt.subplots(nrows=6, ncols=1, figsize=(12,16))

sns.boxplot(x= "Category", y= 'Price', data = df, ax =axes_2[0])
sns.boxplot(x= "GPU", y= 'Price', data = df, ax =axes_2[1])
sns.boxplot(x= "OS", y= 'Price', data = df, ax =axes_2[2])
sns.boxplot(x= "CPU_core", y= 'Price', data = df, ax =axes_2[3])
sns.boxplot(x= "RAM_GB", y= 'Price', data = df, ax =axes_2[4])
sns.boxplot(x= "Storage_GB_SSD", y= 'Price', data = df, ax =axes_2[5])

#Descriptive Statistics
print(df.describe())
print(df.describe(include=object))

#Grouping  "GPU", "CPU_core" and "Price"
df_group = df[['GPU','CPU_core','Price']]
grouped_1 = df_group.groupby(['GPU','CPU_core'], as_index=False).mean()
print(grouped_1)

#Pivot Table
grouped_pivot = grouped_1.pivot_table(index= 'GPU', columns = 'CPU_core')
print(grouped_pivot)


fig3,ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels=grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#moving ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

fig.colorbar(im)

#Pearson Correlation, p-values
data = ['RAM_GB','CPU_frequency','Storage_GB_SSD','Screen_Size_inch','Weight_pounds','CPU_core','OS','GPU','Category']
for param in data:
    pears_coff,p_values = stats.pearsonr(df[param], df['Price'])
    print(param)
    print("The Pearson Coefficient of ",param," is ",pears_coff," and has a P value of P= ",p_values)
