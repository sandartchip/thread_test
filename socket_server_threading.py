import socketserver
import os

HOST = ''
PORT = 50007
MAXTHREAD = 20

class SeroPublisher(object): # 쓰레드 전체 정보 관리하는, 쓰레드 풀 역할 하는 클래스.
    def __init__(self):
        self.threads = []
        self.maxthread = MAXTHREAD

class ThreadedTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f'클라이언트 접속 from {self.client_address[0]}, 요청 받음')

        try:
            self.connectedFlag = True  # self => TCP Handler 객체.
            data = self.request.recv(1024).decode('utf-8')

            while True:
                if data: # 데이터 받았으면
                    print(f"들어온 데이터: {data}")
                    break
                else:
                    continue

                # 1. apple DB 커넥션
                # 2. DB 에서 정보 읽어 오기
                # 3. DB에서 읽어 온 파라미터로 cmd 실행

                # if( len(data) > 0 ):
                #    break

        except self.error:
            print("Error")

        printlist = ['Disconnected from ', self.client_address]

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 50007

    with ThreadedTCPServer( (HOST, PORT), ThreadedTCPHandler ) as server:
        server.serve_forever()
