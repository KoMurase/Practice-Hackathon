import socket

host = '' #使うサーバーの名前
port = #適当なPORT番号

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host,port)) #これでサーバーにつながる

message = 'サーバーの人聞こえますかー'

client.send(message.encode('utf-8')) #適当なデータを送信する

response = client.renv(4096)  #レシーブは
