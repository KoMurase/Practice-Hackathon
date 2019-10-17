import socket

PORT = 50000 #port number

#メイン
#create
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',PORT))

#クライアントからの接続の待ち受け
server.listen()

#クライアントの対応処理
client , addr = server.accept()
client.sendall(b"Hi,oppai\n")
client.close()
server.close()
