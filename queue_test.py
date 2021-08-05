import threading
MAXTHREAD = 2
from queue import Queue
import threading
import time

class WorkerThread(threading.Thread):
    def __init__(self, parent, second, job_id): # 여기서 parent는, worker thread를 생성한 쓰레드 풀 객체 .
        super().__init__()
        self.second = second
        self.parent = parent
        self.job_id = job_id

    def run(self):
        print("sub thread start {}".format(self.second))
        print(" --thread work!! processing!!!!----- {}".format(self.second))
        time.sleep(self.second) # 각 쓰레드에서 처리하는 함수 적어주기.
        print("sub thread end ")

        all_job_dict[self.job_id] = 2  # 작업 완료 -> DB STATUS 변경!!
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


    def make_and_run_new_thread(self, second, job_id):
        print("job submit 요청에 대응하는 새로운 쓰레드 만들기")

        print("현재 쓰레드풀:[[", self.thread_list, "]] \n")

        new_thread = WorkerThread(self, second, job_id) # 새로운 스레드 생성.

        self.lock.acquire()
        self.thread_list.append(new_thread)
        print("쓰레드 리스트 변경 (추가) !!!")
        self.lock.release()

        new_thread.start()
        print("추가 할 쓰레드:", new_thread, "추가 후 쓰레드풀:[[", self.thread_list,"]]" )

    def finish_working_thread(self, finished_thread):

        self.lock.acquire()
        print("현재 쓰레드풀:[[", self.thread_list, "]]  제거 할 쓰레드:", finished_thread)
        self.thread_list.remove(finished_thread)
        print("연산후 쓰레드풀:", self.thread_list)
        self.lock.release()



def return_waiting_job():

    waiting_job_list= []

    for job_id, status in  all_job_dict.items():
        if(status==0):
            waiting_job_list.append(job_id)

    print("------ RETURN WAITING JOB LIST------------------")
    return waiting_job_list

if __name__ == "__main__":
    pool = WorkingThreadPool()

    job_id_list = ['11', '12', '13', '14', '15']
    job_status_list = [0, 0, 0, 0, 0]
    all_job_dict = dict(zip(job_id_list, job_status_list))
    print(all_job_dict)

    while(1):

        time.sleep(5)
        print("----------대기 중 JOB ID 리스트---------")
        waiting_job_list = return_waiting_job()
        print(waiting_job_list )
        print("----------대기 중 JOB ID 리스트---------\n\n")

        print("-----------전체 JOB status------------")
        for row in all_job_dict.items():
            print( row)
        print("-----------전체 JOB END--------")



        for job_id in waiting_job_list:
            if(pool.check_full()==False): # pool이 꽉 차지 않았으면
                print("쓰레드 풀 비어따!!")
                all_job_dict[job_id] = 1 # 실행 중
                pool.make_and_run_new_thread(13, job_id) # second, job

            else:
                print("쓰레드 풀 꽉차서 못넣음..")



