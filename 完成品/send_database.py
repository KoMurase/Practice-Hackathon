import os
import csv
import sys
import mysql.connector
import codecs

FILE = 'catch_text.txt'
DB_HOST='localhost'
DB_DATABASE = 'hackbowl'
DB_USERNAME = 'root'
DB_PASSWORD = 'password'

NAME = 'Murase'
#エラー文テキスト情報が書かれたファイルを開く
if (os.path.exists(FILE)):
    f = open(FILE,'rt')
    data = f.read(1024)
context_er=data.split('IP:')[0]
IP=data.split('IP:')[1]
print('context_er:',context_er)
print('IP:',IP)
#dataには'IP:'の後にユーザーのIPアドレスを含んでいる
#'IP:'で分割してそれぞれを送信

try:
    db = mysql.connector.connect(
     host=DB_HOST,
     database=DB_DATABASE,
     user=DB_USERNAME,
     passwd=DB_PASSWORD
    )
except TypeError,e:
    print(e)
    return None
except:
    print('[Error] DB')
    print('error',sys.exc_info()[0])
    exit()

cur = db.cursor()  #クエリ実行

sql = """SELECT id from users WHERE name='{}''"""
sql = sql.format(IP)
cur.execute(sql)

id = cur.fetchone()
print('id:',id)

sql = """INSERT INTO errors (user_id,body) VALUES({},'{}'')"""
sql = sql.format(id[0],context_er)
cur.execute(sql)
##データベースに送るファイルの読み込み


cur.close()
db.commit()
db.close()
