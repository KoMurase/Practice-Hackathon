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
host = '34.84.0.43'
PORT = 50000
BUFSIZE = 4096
server.bind(('',PORT))
server.listen()

#------database---#
DB_HOST='127.0.0.1'
DB_DATABASE = 'hackbowl'
DB_USERNAME = 'root'
DB_PASSWORD = 'password'

try:
    data = client.recv(BUFSIZE)
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

    sql = """INSERT INTO errors (user_id,body) VALUES({},'{}'')"""
    sql = sql.format(id[0],context_er)
    cur.execute(sql)

    cur.close()
    db.commit()
    db.close()

except:
    print('接続できませんでした')
