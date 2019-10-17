#マルチスレッドに対応できるようにする
import socket
import datetime
import threading

#PORT NUMBER
PORT = 50000
BUFSIZE = 4096

#下請け関数の定義
#client_handler()関数

def client_handler(client,clientno,meg):
    #クライアントの接続処理スレッド
    data = client.recv(BUFSIZE)
    print("(",clientno,")",data.decode('utf-8'))
    client.sendall(msg.encode('utf-8'))
    client.close()

#メインの実行部
#ソケットの作成
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#アドレスの設定
server.bind(('',PORT))
#接続の待ち受け
server.listen()

#クライアントの受付番号の初期化
clientno=0

#クライアントの対応処理
while True:
    client , addr = server.accept() #通信用ソケットの取得
    clientno += 1
    msg = str(datetime.datetime.now())
    print(msg,"接続要求アリ(",clientno,")")
    print(client)

    #スレッドの設定と起動
    p = threading.Thread(target = client_handler,args = (client,clientno,msg))
    p.start()
