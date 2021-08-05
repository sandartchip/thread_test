import threading
MAXTHREAD = 2
from queue import Queue
import threading
import time

class WorkerThread(threading.Thread):
    def __init__(self, parent, second): # 여기서 parent는, worker thread를 생성한 쓰레드 풀 객체 .
        super().__init__()
        self.second = second
        self.parent = parent

    def run(self):
        print("sub thread start {}".format(self.second))
        print(" --processing!!!!----- {}".format(self.second))
        time.sleep(self.second) # 각 쓰레드에서 처리하는 함수 적어주기.
        print("sub thread end ")

        self.parent.finish_working_thread(self) # 쓰레드 풀 pool 객체에 자신을 전달해서, 쓰레드 풀의 working queue에서 remove 시킴
class WorkingThreadPool(object):
    def __init__(self):
        # 쓰레드 전체 정보 관리하는, 쓰레드 풀 역할 하는 클래스.
        self.thread_list = []
        self.max_thread = MAXTHREAD
        self.lock = threading.Lock()

    def get_thread_state(self):
        print("쓰레드 전체 갯수", self.max_thread)

    def check_full(self):
        if( len( self.thread_list) >= MAXTHREAD ):
            return True
        else:
            return False


    def make_and_run_new_thread(self, second):
        print("job submit 요청에 대응하는 새로운 쓰레드 만들기")

        print("현재 쓰레드풀:[[", self.thread_list, "]] ")

        if( len(self.thread_list) < self.max_thread):
            new_thread = WorkerThread(self, second) # 새로운 스레드 생성.

            self.lock.acquire()
            self.thread_list.append(new_thread)
            print("쓰레드 리스트 변경 (추가) !!!")
            self.lock.release()

            new_thread.start()
            print("추가 할 쓰레드:", new_thread, "추가 후 쓰레드풀:[[", self.thread_list,"]]" )
        else:
            print("쓰레드 풀 꽉차서 못넣음..")

    def finish_working_thread(self, finished_thread):

        self.lock.acquire()
        print("현재 쓰레드풀:[[", self.thread_list, "]]  제거 할 쓰레드:", finished_thread)
        self.thread_list.remove(finished_thread)
        print("연산후 쓰레드풀:", self.thread_list)
        self.lock.release()

def return_waiting_job():

    waiting_job_dict = {}

    for index, job_id in enumerate( job_id_list):
        if(job_status_list[index]==0):
            waiting_job_dict[job_id]=0

    #waiting_job_dict = dict( zip( job_id_list, job_status_list))
    print("------ RETURN WAITING JOBS ------------------")
    return waiting_job_dict

if __name__ == "__main__":
    pool = WorkingThreadPool()

    job_id_list = ['11', '12', '13', '14', '15']
    job_status_list = [0,0,0,0,0]

    while(1):
        waiting_job_dict = return_waiting_job()
        print(waiting_job_dict)

        time.sleep(5)




    pool.make_and_run_new_thread(4)
    pool.make_and_run_new_thread(4)
    pool.make_and_run_new_thread(4)
    pool.make_and_run_new_thread(4)
    pool.make_and_run_new_thread(4)
    pool.make_and_run_new_thread(4)