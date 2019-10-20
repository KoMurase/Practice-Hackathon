import os
import csv
import sys
import mysql.connector
import codecs

FILE = 'catch_text.txt'
DB_HOST='loclhost'
DB_DATABASE = 'hackbowl'
DB_USERNAME = 'root'
DB_PASSWORD = 'password'
data = 'errorIP:10000'
context_er=data.split('IP:')[0]
IP=data.split('IP:')[1]
print('context_er:',context_er)
print('IP:',IP)
#try:
db = mysql.connector.connect(
     host=DB_HOST,
     database=DB_DATABASE,
     user=DB_USERNAME,
     passwd=DB_PASSWORD
    )

except TypeError,e:
    print(e)

except:
    print('[Error] DB')
    print('error',sys.exc_info()[0])
