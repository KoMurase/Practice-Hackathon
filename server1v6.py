import socket
import datetime

#PORT NUMBER
PORT = 50000

#メイン
#ソケットの作成
server = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)

#アドレスの設定
server.bind(('',PORT))

#接続の待ち受け
server.listen()

#クライアントの対応処理
while True:
    client , addr = server.accept()
    msg = str(datetime.datetime.now())
    client.sendall(msg.encode('UTF-8'))
    print(msg,'接続要求アリ')
    print(client)
    client.close()
