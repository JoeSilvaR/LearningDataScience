# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:11:10 2023

@author: josep
"""
### Imports ###
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
### Functions ###

#function to download data
def download(url, filename):
    respone = requests.get(url)
    if respone.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(respone.content)
            
### Main Code ###

# downloading and storing data in a dataframe           
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
            
download(filename,  "diabetes.csv")

df = pd.read_csv( "diabetes.csv")

#viewing the data
df.head() #viewing first few rows and columns of dataframe
df.shape # viewing the dimensions of dataframe
df.info() # viewing info of dataframe, dtypes, columns etc

# confirming data types
df.dtypes
# statistical overview of data
df.describe()


#handling missing values
missing_data = df.isnull()
missing_data.head()

#counting the amount of missing data, False indicates no missing values
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
    
#Visualization
labels = 'Diabetic', 'Not Diabetic'
plt.pie(df['Outcome'].value_counts(), labels=labels, autopct='%0.02f%%')
plt.legend()
plt.show()

list_b =[1,3,4,5,8,7]
list_b.sort()


