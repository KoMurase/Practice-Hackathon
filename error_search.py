import sys
import os
ERROR_FILE = './error.txt'
SIZE_MEMO = './SIZE_MEMO.txt'

#socket通信用
import socket
import sys
HOST = "localhost"
PORT = 50000
BUFSIZE = 4096 #受信バッファの大きさ
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
f = open(ERROR_FILE,'rt')

before_size = os.path.getsize(SIZE_MEMO)
file_size=os.path.getsize(ERROR_FILE)

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
    client.sendall(message.encode('utf-8'))
    print("Done Sending")

    client.close()
