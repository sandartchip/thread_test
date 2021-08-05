from enum import Enum
import pymysql
# state -> 0

class StatusCode(Enum):
    waiting = 0
    running = 1
    finished = 2

class DatabaseObject:
    def connect(self):
        self.sero_db_conn = pymysql.connect(
            user='root',
            passwd='1234',
            # host='127.0.0.1',
            host='apple.snu.ac.kr',
            db='soyeon_pj',
            port=3308,
            charset='utf8'
        )

    def make_cursor(self):
        self.cursor = self.sero_db_conn.cursor(pymysql.cursors.DictCursor) # DB에서 데이터 패칭 해오는 변수

    def fetch_data(self, folder_id):

        folder_id = str(189 + int(folder_id))  # 로 가지고 오거나 아니면 Folder name 외래키 참조로 .

        query = "SELECT * FROM soyeon_pj_job WHERE result_folder_id=%s"

        self.cursor.execute(query, (folder_id))

        result = self.cursor.fetchall()  # 데이터 패치

        print("-----------------------출력 시작-----------", folder_id)

        for r in result:
            print(r['id'], r['depth'], r['phred_quality'], r['evalue'], r['identity'], r['coverage'],
                  r['result_folder_id'])
        # os.cmd(f"python main.py -c {coverage} ")

        print("-----------------------출력 끝-----------", folder_id)

    def check_waiting_job(self): # 아직 run하지 않은 JOB들의 목록을 DB에서 가져 온다.
        query = f"select * from soyeon_pj_job WHERE state={StatusCode.waiting}"

        try:
            self.cursor.execute(query)

            for row in self.cursor.fetchall():
                print(row)
        except pymysql.Error as e:
            print("에러")


    def close_connection(self):
        self.sero_db_conn.close()
