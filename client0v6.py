import socket

HOST = "localhost"
#HOST = '::1'
PORT = 50000
BUFSIZE = 4096 #受信バッファの大きさ

#メイン実行部
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
#サーバとの接続
client.connect((HOST,PORT))

#サーバからのメッセージの受信
data = client.recv(BUFSIZE)
print(data.decode('UTF-8'))

client.close()
