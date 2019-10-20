#server用
import socket
import datetime

#database用
import os
import csv
import sys
import mysql.connector
import codecs

#-----server------#
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'localhost'
PORT = 50000
BUFSIZE = 4096
server.bind(('',PORT))
server.listen()

#------database---#
DB_HOST='127.0.0.1'
DB_DATABASE = 'hackbowl'
DB_USERNAME = 'root'
DB_PASSWORD = 'password'

while True:
    client, addr = server.accept()
    print(addr)
    d=datetime.datetime.now()
    fname = d.strftime('%m%d%H%M%S%f')
    print(fname,'接続要求あり')
    print(client)
    #fout = open(fname + '.txt','wt')  #書き込みファイル
    #fout = open('catch_text'+ '.txt','wt')
    #print(data.decode('utf-8'),file=fout)
    print("Receiving...")
    
    try:

        #ここから受け取った文字列を見る
        while True:
            data = client.recv(BUFSIZE)
            data = data.decode('utf-8')
            if not data: #受け取るデータがない場合
                break


            #data = f.read(1024)
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
            except TypeError as e:
                print(e)

            except:
                print('[Error] DB')
                print('error',sys.exc_info()[0])
                exit()

            try:

                cur = db.cursor()  #クエリ実行

                sql = """SELECT id from users WHERE name='{}''"""
                sql = sql.format(IP)
                cur.execute(sql)

                id = cur.fetchone()
                print('id:',id)
                print(type(id))

                sql = """UPDATE errors SET resolution = true WHERE user_id = {}"""
                sql = sql.format(id[0])
                cur.execute(sql)

                sql = """INSERT INTO errors (user_id,body) VALUES({},'{}')"""
                sql = sql.format(id[0],context_er)
                cur.execute(sql)

                cur.close()
                db.commit()
                db.close()
            except TypeError as e:
                print(e)
            except:
                print('データベースで接続できませんでした.')
    except TypeError as e:
        print(e)
    except:
        print('エラー発生しました.接続を中止します')

    client.close()
