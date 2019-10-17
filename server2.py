import socket
import datetime

#PORT NUMBER
PORT = 50000
BUFSIZE = 4096

#メイン
#ソケットの作成
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#アドレスの設定
server.bind(('',PORT))

#接続の待ち受け
server.listen()

#クライアントの対応処理
while True:
    client , addr = server.accept() #通信用ソケットの取得
    msg = str(datetime.datetime.now())
    print(msg,'接続要求アリ')
    print(client)

    data = client.recv(BUFSIZE)
    print(data.decode('UTF-8'))

    client.sendall(msg.encode('utf-8'))
    client.close()
