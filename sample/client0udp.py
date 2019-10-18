import socket

HOST = 'localhost'
PORT = 50000
BUFSIZE = 4096

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b'Hey! ',(HOST,PORT))

#サーバーからのメッセージの受信
data = client.recv(BUFSIZE)
print(data.decode('UTF-8'))

#ソケットのクローズ
client.close()
