import socket
import datetime

#PORT NUMBER
PORT = 50000
BUFSIZE = 4096
#メイン
#ソケットの作成
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#アドレスの設定
server.bind(('',PORT))

#クライアントの対応処理
while True:
    data, client = server.recvfrom(BUFSIZE)
    msg = str(datetime.datetime.now())
    server.sendto(msg.encode('UTF-8'),client)
    print(msg,'接続要求アリ\n')
    print(client)
    #server.close()
