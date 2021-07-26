
import threading, queue, time

data = 0

lock = threading.Lock()

def generator(start, end):
    global data;

    for i in range(start, end, 1):
        lock.acquire() # lock 설정, 다음 이 lock 호출할 때 쓰레드는 대기

        buf = data
        time.sleep(0.01)
        data = buf + 1

        lock.release()

# generator 함수를 두 개의 쓰레드로 실행함
t1 = threading.Thread(target=generator, args = (1, 10))
t2 = threading.Thread(target=generator, args = (1, 10))

t1.start()
t2.start()

t1.join()
t2.join()

print(data)