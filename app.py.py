#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pywebio.input import *
from pywebio.output import *

input("What's your name?")
select("Select food", ['Orange','Apple'])
checkbox("Are you okay?",  options=["I'm Okay."])
radio("What do you like to do?", options=['Eat','Sleep','Study'])


# In[ ]:


pip install pywebio


# In[ ]:


from pywebio.input import *
from pywebio.output import *

input("What's your name?")
select("Select food", ['Orange','Apple'])
checkbox("Are you okay?",  options=["I'm Okay."])
radio("What do you like to do?", options=['Eat','Sleep','Study'])


# In[ ]:


from pywebio.output import *
from pywebio.input import *
import time

put_markdown('## Hello there')

put_text("I hope you are having a great day! Here is our menu")

put_table([
    ['Food','Price'],
    ['Noodle',10],
    ['Chicken and Rice', 11]
])
    
with popup("Subscribe to the page"):
    put_text("Join other Foodies!")
    
food = select("Choose your favorite food", ['Noodle','Chicken and Rice'])
    
put_text(f"You choose {food}. Please wait until it is served!")
    
put_processbar('bar')
for i in range(1,11):
    set_processbar('bar',i/10)
    time.sleep(0.1)
put_markdown("Here is your food! Enjoy!")

if food =='noodle':
    put_image(open('C:/Users/Owner/Desktop/Website/Schezwan-Noodles-1014x1536.jpeg','rb').read())
else:
    put_image(open('C:/Users/Owner/Desktop/Website/chinese-chicken-and-rice.jpeg','rb').read())
    
put_file("You can download the food here",b"Hello")


# In[ ]:


#import sweetviz as sv
import pandas as pd
from pywebio.input import file_upload
from pywebio.output import put_html, put_loading
from pywebio.output import *
from pywebio.input import *
from pywebio import start_server
import csv 
import re
import tabula as tb

put_markdown('## Hello there')

put_text("Please upload pdf file")

def app():
    file = file_upload(label='Upload your pdf file', accept='.pdf')
    #content = file['content'].decode('utf-8').splitlines()

    df = tb.read_pdf("C:/Users/Owner/Desktop/scrapy/test/Test 2/pscd-dalhousie-university-2022.pdf",pages="all")
    print(len(df))


# In[ ]:


from pywebio.input import *
from pywebio.output import *
import csv

input("What's your name?")
select("Select food", ['Orange','Apple'])
checkbox("Are you okay?",  options=["I'm Okay."])
radio("What do you like to do?", options=['Eat','Sleep','Study'])


# In[ ]:


import csv
import os
import pandas as pd

file_dict = {}
for subdir, dirs, files in os.walk("C:/Users/Owner/Desktop/scrapy/test/final"):
    for file in files:
        filepath = subdir + os.sep + file
        # you can have multiple endswith
        if filepath.endswith((".csv", ".CSV")):
            file_dict[file] = filepath
            print(file)

#read the path
file_path = "C:/Users/Owner/Desktop/scrapy/test/final"
#list all the files from the directory
file_list = os.listdir(file_path)
print(file_list)

df_append = pd.DataFrame()
#append all files together
for file in file_list:
    df_temp = pd.read_csv(file)
    df_append = df_append.append(df_temp, ignore_index=True)
df_append.to_csv(C:/Users/Owner/Desktop/scrapy/test/final/combined.csv")


# In[ ]:


import csv
import os
import pandas as pd

file_dict = {}
for subdir, dirs, files in os.walk("C:/Users/Owner/Desktop/scrapy/test/final"):
    for file in files:
        filepath = subdir + os.sep + file
        # you can have multiple endswith
        if filepath.endswith((".csv", ".CSV")):
            file_dict[file] = filepath
            print(file)


combined_csv = pd.concat([pd.read_csv(file) for file in file_dict])
combined_csv.to_csv( "C:/Users/Owner/Desktop/scrapy/test/final/combined_csv.csv", index=False, encoding='utf-8-sig')


# In[ ]:


import os
import glob
import pandas as pd
import csv
os.chdir("C:/Users/Owner/Desktop/scrapy/test/final")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

#combine all files in the list
combined = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined.to_csv( "C:/Users/Owner/Desktop/scrapy/test/final/combined.csv", index=False, encoding='utf-8-sig')


# In[ ]:


import csv
import os
import pandas as pd
import pywebio
import glob
from pywebio.input import *
from pywebio.output import *

os.chdir("C:/Users/Owner/Desktop/scrapy/test/final")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

df = pd.read_csv("C:/Users/Owner/Desktop/scrapy/test/final/test0.csv")

select("Select University", ['CBU','Dalhousie'])
input("Type the name of Prof.")
pywebio.put_table([
    ['Name','Salary']
    ['Barrett, David','114382']
    

     


# In[ ]:


from pywebio.input import *
from pywebio.output import put_html, put_loading
from pywebio import start_server
import csv 
import pandas as pd
import re

def app():
     file = file_upload(label='Upload CSV file', accept='.csv')
     content = file['content'].decode('utf-8').splitlines()
     df = list_to_dataframe(content)
     columns = list(df.columns)
     target = select("Select target variable", columns)
     columns.remove(target)
    
if __name__=='__main__':
     start_server(app, debug=True)


# In[ ]:


from pywebio.input import textarea, input
from pywebio import start_server


def app():
    text = textarea("Please insert the text for your PDF file", 
                    placeholder="Type anything you like", 
                    required=True)
                    
    save_location = input("What is the name of your PDF file?", required=True)
    #put_text("Congratulations! A PDF file is generated for you.")


if __name__ == '__main__':
    start_server(app, port=36535, debug=True)


# In[ ]:


pip install pywebio pymongo dnspython pandas plotly


# In[ ]:


# importing flask
from flask import Flask, render_template
  
# importing pandas module
import pandas as pd
  
  
app = Flask(__name__)
  
  
# reading the data in the csv file
df = pd.read_csv('C:/Users/Owner/Desktop/scrapy/test/final/test0.csv')
df.to_csv('C:/Users/Owner/Desktop/scrapy/test/final/combine.csv', index=None)
  
  
# route to html page - "table"
@app.route('/')
@app.route('/table')
def table():
    
    # converting csv to html
    data = pd.read_csv('C:/Users/Owner/Desktop/scrapy/test/final/test0')
    return render_template('table.html', tables=[data.to_html()], titles=[''])
  
  
if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))


# In[ ]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


# In[ ]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Professors (Name VARCHAR(255), Salary VARCHAR(255))")


# In[ ]:


import pathlib
from pathlib import Path
Path('my_data.db').touch()


# In[ ]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


# In[5]:


import sqlite3
conn = sqlite3.connect('my_data.db')
c = conn.cursor()


# In[6]:


c.execute('''CREATE TABLE universities (Name text, Salary int)''')


# In[10]:


import pandas as pd
# load the data into a Pandas DataFrame
universities = pd.read_csv('C:/Users/Owner/Desktop/scrapy/test/final/test1.csv')
# write the data to a sqlite table
universities.to_sql('universities', conn, if_exists='append', index = False)


# In[11]:


c.execute('''SELECT * FROM universities''').fetchall()


# In[4]:


import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")


# In[ ]:




