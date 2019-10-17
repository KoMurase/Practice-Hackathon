import socket
#Ipv4による実装
#グローバル変数
HOST = 'localhost'
#HOST = 127.0.0.1 接続先のホスト名
PORT = 50000 #ポート番号
BUSIZE = 4096

#メインの実行
#ソケットの作成

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#サーバとの接続
client.connect((HOST,PORT))

#サーバからのデータ受信
data = client.recv(BUSIZE)
print(data.decode('UTF-8'))

#コネクションのクローズ
client.close()
