import sys
import os
ERROR_FILE = './error.txt'
BEFORE_SIZE = './BEFORE_SIZE.txt'

#socket通信用
import socket
import sys

HOST = "localhost"
#HOST = #太一のPC
PORT = 50000
BUFSIZE = 4096 #受信バッファの大きさ
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

f = open(ERROR_FILE,'rt')
b = open(BEFORE_SIZE,'rt')
before_size = b.read(1024)
before_size = int(before_size)
print(before_size)
print(type(before_size))

#ipアドレス

ip = socket.gethostbyname(HOST) ##ユーザーのipアドレス

#client.close()

if before_size=='':
    before_size=0

file_size=os.path.getsize(ERROR_FILE)

fout = open(BEFORE_SIZE,'wt')
#print(file_size.decode('utf-8'),file=fout)
print(file_size,file=fout)

if before_size == file_size:
    print('以前と同じエラー(大きさ)です')

else:

    ###ここでソケットを通じてサーバーに送る
    try:
        #サーバとの接続
        client.connect((HOST,PORT))
    except:
        print('接続できませんでした')
        sys.exit()

    print('Sending...')
    message = f.read(1024)
    data = message+'IP:'+ip
    client.sendall(str(data).encode('utf-8'))
    print("Done Sending")


    client.close()
