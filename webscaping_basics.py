# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:41:47 2023

@author: joseph S.
"""

### Installs ###

#!pip install html5lib


###Imports ###
from bs4 import BeautifulSoup
import requests
###Functions ###


#### Main Code ###


html ="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')
print(soup.prettify())

## Tags ##
tag_object = soup.title
print("tag_object: ", tag_object)

tag_object = soup.h3
print('tag_object:', tag_object)

## Children, Parent, Siblings ##
tag_child = tag_object.b
print("tag_child: ", tag_child)

parent_tag = tag_child.parent
print('parent_tag', parent_tag)

sibling_1 = tag_object.next_sibling
print('sibling_1:',sibling_1)

sibling_2 = sibling_1.next_sibling
print('sibling_2: ', sibling_2)

sibling_3 = sibling_2.next_sibling
print('sibling_3: ', sibling_3)

## HTML Attributes ##

tag_child['id'] #finding tag attributes

tag_child.attrs #accessing dictonary of attributes for a tag

tag_child.get('id') #using get to obtain tag attributes

# Converting tag type to NAVAGABLE str which is a type element of bs4
#that allows for some bs4 functionallity
tag_string = tag_child.string
print(tag_string)
type(tag_string)

#Converting back to Python/Unicode str
unicode_str = str(tag_string)
unicode_str

## Filter ##

#New Data, Rocket Launch Table
'''%%html
<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>
'''

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')

#extracting all tags with the same name and its children
table_rows = table_bs.find_all('tr')
table_rows

#can iterate like a list
first_row = table_rows[0]
first_row

#obtaining the child
first_row.td

# each element corresponds to a row in a table

for i,row in enumerate(table_rows):
    print('row',i, 'is',row)

# use the find_all() method to organize the children tags into rows and columns
for i, row in enumerate(table_rows):
    print('row', i)
    cells = row.find_all('td')
    for j,cell in enumerate(cells):
        print('column',j, 'cells',cell)

#can find and amtch items in a list
list_inputs = table_bs.find_all(name=['tr','td'])
list_inputs

## Attributes ##

table_bs.find_all(id= 'flight')#extracting info based on id variable

#finds all elements with links to Florida Wikipedia page
list_input = table_bs.find_all(href ="https://en.wikipedia.org/wiki/Florida")  
list_inputs

table_bs.find_all(href=True) #finds all links with relevant info

table_bs.find_all(href=False)

soup.find_all(id ='boldest')

