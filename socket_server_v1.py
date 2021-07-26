import socket
import random

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('서버가 시작되었습니다.')

    conn, addr = s.accept()

    with conn:
        answer = random.randint(1, 9)
        print(f'클라이언트가 접속했습니다:{addr}, 정답은 {answer} 입니다.')

        while True:
            data = conn.recv(1024).decode('utf-8')
            # 클라이언트가 보낸 sendall을, receive받는다.
            print(f'데이터:{data}')

            try:
                conn.sendall("정상 전달 완료".encode('utf-8'))
            except ValueError:
                conn.sendall('전달된 값 Error !!'.encode('utf-8'))

            if( len(data)>0):
                print("exit the connection")
                break
