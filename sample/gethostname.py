import socket #モジュールのインポート
while True:
    try:
        hostname = input('ホスト名入力(qで終了)')
        if hostname == 'q':
            #終了
            break
        print(socket.gethostname(hostname))

    except:
        print('変換できませんでした')
