import socket
import sys

PORT = 50000
BUFSIZE = 4096

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF_INET6 でIPv6を
#socket.SOCK_STREAMでTCP通信を指定している

#サーバとの通信
host = input('接続先のサーバ:')
try:
    client.connect((host,PORT))
except:
    print('接続できません')
    sys.exit()
#サーバへのメッセージ送信
msg = input('write message : ')
client.sendall(msg.encode('utf-8'))

#サーバからのメッセージの受信
data = client.recv(BUFSIZE)
print('サーバからのメッセージ : ')
print(data.decode('utf-8'))

client.close()
