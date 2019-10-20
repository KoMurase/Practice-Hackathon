#ソケット通信用
import socket
import datetime

#データベース用
import os
import csv
import sys
import mysql.connector
import codecs

#各種定義
FILE = 'catch_text.txt'

DB_HOST='localhost'
DB_DATABASE = 'hackbowl'
DB_USERNAME = 'root'
DB_PASSWORD = 'password'

server = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
host = 'localhost'
PORT = 50000
BUFSIZE = 4096
server.bind(('',PORT))
server.listen()

while True:
    client, addr = server.accept()
    print(addr)
    d=datetime.datetime.now()
    fname = d.strftime('%m%d%H%M%S%f')
    print(fname,'接続要求あり')
    print(client)
    #fout = open(fname + '.txt','wt')  #書き込みファイル
    fout = open('catch_text'+ '.txt','wt')
    #print(data.decode('utf-8'),file=fout)
    print("Receiving...")

    try:
        #ここから受け取った文字列を見る
        while True:
            data = client.recv(BUFSIZE)
            if not data: #受け取るデータがない場合
                break
            print(data.decode('utf-8')+'\n')
            print(data.decode('utf-8'),file=fout)#ファイルへの書き込み
    except:
        print('エラー発生しました.接続を中止します')
    client.close()
    fout.close()

#--------------------------------------------------#
#ここからデータベース
#--------------------------------------------------#

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


sql = """INSERT INTO errors (users(id),body) VALUES({},{})"""
sql = sql.format(IP,context_er)
##データベースに送るファイルの読み込み

cur.close()
db.commit()
db.close()
