from socketserver import StreamRequestHandler
from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer
import os, time
import threading
import pymysql


from sero_db_control import DatabaseObject

HOST = ''
PORT = 50007
MAXTHREAD = 5

def check_db_status():
    try:
        query = "select * from soyeon_pj_job WHERE state = 'wait' );" # JOB의 상태는 wait, runninng, finish 로 구분

    except :
        print("DB 접속 에러 발생")



def connect_db_fetch_data( folder_id ):
    sero_db_conn = pymysql.connect(
        user='root',
        passwd='1234',
        #host='127.0.0.1',
        host= 'apple.snu.ac.kr',
        db='soyeon_pj',
        port=3308,
        charset='utf8'
    )
    cursor = sero_db_conn.cursor(pymysql.cursors.DictCursor)

    folder_id = str( 189 + int(folder_id)  )# 로 가지고 오거나 아니면 Folder name 외래키 참조로 .

    query = "SELECT * FROM soyeon_pj_job WHERE result_folder_id=%s"

    #query = "SELECT * FROM `soyeon_pj_job`"

    cursor.execute(query, (folder_id))

    result = cursor.fetchall() # 데이터 패치

    print("-----------------------출력 시작-----------", folder_id)

    for r in result:
        print (r['id'], r['depth'], r['phred_quality'], r['evalue'], r['identity'], r['coverage'], r['result_folder_id'])
    # os.cmd(f"python main.py -c {coverage} ")

    print("-----------------------출력 끝-----------", folder_id)

    sero_db_conn.close()

class WorkerThread(threading.Thread): # 실제로 작업을 수행 중인 쓰레드.
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("sub thread start {}".format(self.name))
        time.sleep(3)
        print("sub thread end")


class SeroThreadPool(object):
    def __init__(self):
        # 쓰레드 전체 정보 관리하는, 쓰레드 풀 역할 하는 클래스.
        self.thread_list = []
        self.max_thread = MAXTHREAD

    def get_thread_state(self):
        print("쓰레드 전체 갯수", self.max_thread)

    def make_new_thread(self, name):
        print("job submit 요청에 대응하는 새로운 쓰레드 만들기")
        new_thread = WorkerThread(self, name) # 새로운 스레드 생성.
        self.thread_list.append(new_thread)

class ThreadedTCPHandler(BaseRequestHandler):
    # JOB Submit 요청 시
    def handle(self):
        print(f'클라이언트 접속 from {self.client_address[0]}, 요청 받음')

        try:
            self.connectedFlag = True  # self => TCP Handler 객체.
            data = self.request.recv(1024).decode('utf-8')

            while True:
                if data: # 데이터 받았으면
                    print(f"들어온 데이터: {data}")
                    sum =0
                    time.sleep(2)
                    print(f"끝끝 - {data}")

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

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

if __name__ == "__main__":

    pool = SeroThreadPool()
    # 쓰레드 풀 클래스를 인스턴스화 시킴.
    # 쓰레드풀은 전체 쓰레드를 관리하므로, 1개만 있으면 됨.

    '''
        wait from client 
    '''
    HOST, PORT = "localhost", 50007

    sero_db = DatabaseObject()

    while 1:
        try:
            sero_db.connect()
            print("연결 완료")
            sero_db.make_cursor()
            sero_db.fetch_data(9) ##TODO:: 수정
            break

        except pymysql.Error as e:
            print("에러 %d, %s" % (e.args[0], e.args[1]))
            print("재시도 중입니다....")
            time.sleep(5)
            sero_db.connect()
            print("연결 완료")
            sero_db.make_cursor()
            sero_db.fetch_data(9)  ##TODO:: 수정

#    with ThreadedTCPServer( (HOST, PORT), ThreadedTCPHandler ) as server:
#        server.serve_forever()
