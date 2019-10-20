
import sys
import os
ERROR_FILE = './error.txt'

#socket通信用
import socket
import sys

HOST = '34.84.0.43'
PORT = 50000
BUFSIZE = 4096 #受信バッファの大きさ
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

before_size = 0
connect_flag = True

while True:
    #ERROR_FILEを開くためにエラー処理を行う

    if (os.path.exists(ERROR_FILE)):
        f = open(ERROR_FILE,'rt')
        message = f.read(1024)

        file_size=os.path.getsize(ERROR_FILE)

        if before_size != file_size:
            ip = socket.gethostbyname(socket.gethostname()) ##ユーザーのipアドレス

            ###ここでソケットを通じてサーバーに送る
            try:
                #サーバとの接続
                if connect_flag:
                    client.connect((HOST,PORT))
                    connect_flag = False


            except TypeError as e:
                print(e)

            except:
                print('接続できませんでした')
                sys.exit()

            print('Sending...')

            data = message+'IP:'+ip
            client.sendall(str(data).encode('utf-8'))
            print("Done Sending")


            # client.close()

        before_size = file_size
