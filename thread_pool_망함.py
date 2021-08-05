from threading import Thread
import sys, random
from queue import Queue
import time

def Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)

        self.tasks = tasks
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()

            try:
                func(*args, **kargs)
            except Exception as e:
                print(e)
            finally:
                self.tasks.task_done()

class ThreadPool: # 대기 큐로부터 작업을 소비하는 쓰레드 풀

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)

        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put( (func, args, kargs) )

    def map(self, func, args_list):

        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        self.tasks.join()

def find_users_sync(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        time.sleep(1)
    print(f'> 총 {n} 명 사용자 멀티 쓰레드  조회 완료!')

def test():
    print(pool222)

def test3():
    print(pool222)

if __name__ == "__main__":
    from random import randrange
    from time import sleep


    pool222=333
    #    pool = ThreadPool(4)
    test3()
'''
    delay1 = random.randint(1, 9)
    delay2 = random.randint(1, 9)
    delay3 = random.randint(1, 9)

    pool.add_task( find_users_sync, delay1 )
    pool.add_task( find_users_sync, delay2 )
    pool.add_task( find_users_sync, delay3 )

    pool.wait_completion()
'''