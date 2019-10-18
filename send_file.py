import socket
import sys
HOST = "localhost"
PORT = 50000
BUFSIZE = 4096 #受信バッファの大きさ
DATAFILE = './error.txt'
#メイン実行部
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
f = open(DATAFILE,'rt')

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
