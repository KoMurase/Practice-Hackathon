import socket

host = '' #使うサーバーの名前
port = #適当なPORT番号

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定し,バインドする
serversock.listen(10)   #接続の待ち受けをする (キューの最大値を指定)

print('接続中...')
clientsock,client_address = serversock.accept() #接続されたデータを格納

while True:
    rcmsg = clientsock.recv(1024)
    print('Received -> %s' %(rcmsg))
    if rcmsg== '':
        break
    print('Type message...')

    s_msg = input().replace('b', '').encode('utf-8')
    if s_msg =='':
        break
    print('ちょ待って')

    clientsock.sendall(s_msg)  #メッセージを返す
clientsock.close()
