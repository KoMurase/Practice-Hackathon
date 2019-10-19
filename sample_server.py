import socket
import datetime
server = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
#host = 'localhost'
PORT = 50000
BUFSIZE = 4096
server.bind(('',PORT))
server.listen()
#f = open('error.txt','wb')

while True:
    client, addr = server.accept()
    print(addr)
    d=datetime.datetime.now()
    fname = d.strftime('%m%d%H%M%S%f')
    print(fname,'接続要求あり')
    print(client)
    #fout = open(fname + '.txt','wt')  #書き込みファイル
    fout = open('catch_text'+ '.txt','wt')
    #print(data.decode('utf-8'),file=fout)
    print("Receiving...")

    try:
        #ここから受け取った文字列を見る
        while True:
            data = client.recv(BUFSIZE)
            if not data: #受け取るデータがない場合
                break
            print(data.decode('utf-8')+'\n')
            print(data.decode('utf-8'),file=fout)#ファイルへの書き込み
    except:
        print('エラー発生しました.接続を中止します')
    client.close()
    fout.close()
