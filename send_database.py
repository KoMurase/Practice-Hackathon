import os
import csv
import sys
import mysql.connector

import codecs
"""
DB_USER=root
DB_PASSWORD=password
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=hackbowl
SERVER_PORT=8080
APP_DOTENV_PATH=OK
"""
FILE = 'catch_text.txt'

DB_HOST = 'localhost'
DB_DATABASE = 'splaDB'
DB_USERNAME = 'root'
DB_PASSWORD = ''

#エラー文テキスト情報が書かれたファイルを開く
if (os.path.exists(FILE)):
    f = open(FILE,'rt')
    data = f.read(1024)
context_er=data.apply(lambda x: x.split('IP:')[0])
IP=data.apply(lambda x: x.split('IP:')[1])
print('context_er:',context_er)
print('IP:',IP)
#dataには'IP:'の後にユーザーのIPアドレスを含んでいる
#'IP:'で分割してそれぞれを送信
"""
try:
    db = mysql.connector.connect(
    host =  ,
    database = ,
    user = ,
    passwd =
    )
except:
    print('[Error] DB接続失敗')
    exit()

cur = db.cursor()
"""

##データベースに送るファイルの読み込み
