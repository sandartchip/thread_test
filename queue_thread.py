
from queue import Queue
import threading
import time

def push(q):
    print('thread1 start')
    time.sleep(5)
    q.put('Zero')
    print("push! 0")

    q.put('One')
    print("push! 1")

    q.put('Two')
    print("push! 2")

    q.put('Three')
    print("push! 3")

    q.put('Four')
    print("push! 4")

    time.sleep(5)

    q.put('Five')
    print("push! 5")

    q.put('Six')
    print("push! 6")

    q.put('Seven')
    print("push! 7")


    time.sleep(5)

    q.put('Five')
    print("push! 5")

    q.put('Six')
    print("push! 6")

    q.put('Seven')
    print("push! 7")

    time.sleep(5)

    q.put('Eight')
    print("push! 8")

    q.put('Nine')
    print("push! 9")

    time.sleep(5)

    q.put('Ten')
    print("push! 10")
    time.sleep(5)

def pop(q):
    print("Thread2 start")

    while( True ):
        test = q.get() # 큐의 내용을 얻어 옴, 마이너스 됨 .

        if (test):
            time.sleep(1)
            print(test)
            print("큐 사이즈:",q.qsize())

            '''if(q.qsize()==0):
                print("큐가 빔")
                break
            '''



if __name__ == "__main__":
    queue = Queue()
    thread1 = threading.Thread(target = push, args=(queue,)) # 생산자 쓰레드 생성
    thread2 = threading.Thread(target = pop, args=(queue, )) # 소비자 쓰레드 생성

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

