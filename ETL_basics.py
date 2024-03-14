# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:29:57 2023

@author: josep
"""
### imports ###
import pandas as pd
import seaborn
import numpy as np
import json
import requests

# Transforming Data
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df

df_t1 = df.transform(func = lambda x: x+10)
df_t1

df_sq = df.transform(func = ['sqrt'])
df_sq

## Json files ##

#json file format
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open('person.json', 'w') as f:
    json.dump(person, f)

# serializing json
json_object = json.dumps(person, indent =4)

#writing to sample.json

with open('smaple.json', 'w') as outfile:
    outfile.write(json_object)
print(json_object)    

#reading from a json file

with open('person.json', 'r') as openfile:
    json_object = json.load(openfile)
    
print(json_object)
type(json_object)

## XLSX File ##

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

def download(url,filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
            
download(filename, "file_example_XLSX_10.xlsx")
df = pd.read_excel("file_example_XLSX_10.xlsx", header=None)
df

#Creating xml documents with python built in module xml.etree.ElementTree 
#the above is a low-level pibrary for creating and parsing xml documents
import xml.etree.ElementTree as ET

#creating file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details,'firstname')
second = ET.SubElement(details,'lastname')
third = ET.SubElement(details, 'age')
first.text= 'Shiv'
second.text= 'Mishra'
third.text= '23'

#creating a new xml file with the results
mydata1=ET.ElementTree(employee)

myfile= open('items2.xml', 'wb')
myfile.write(mydata1)
with open('new_sample.txt', 'wb') as files:
    mydata1.write(files)

#Reading and parsin an XML document
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"

def download(url,filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

download(filename,"Sample-employee-XML-file.xml")

#parsing an XML document and creating a list of columns to construct dataframe

tree = ET.parse("Sample-employee-XML-file.xml")
root = tree.getroot()

columns = ["firstname", "lastname", "title", "division", "building","room"]

dataframe = pd.DataFrame(columns = columns)

for node in root:
    firstname = node.find('firstname').text
    lastname = node.find('lastname').text
    title = node.find('title').text
    division = node.find('division').text
    building = node.find('building').text
    room = node.find('room').text
    
dataframe = dataframe.append(pd.Series(["firstname", "lastname", "title", "division", "building","room"],
                         index =columns), ignore_index=True)
dataframe
