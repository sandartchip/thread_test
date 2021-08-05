from threading import Thread
import time


def find_users_sync(n):
    num = 0
    for i in range(1, 1000000000):
        num += i
        #time.sleep(1)
    print(f'> 총 {num} 명 사용자 멀티 쓰레드  조회 완료!')


if __name__ == "__main__":
    start =time.time()

    th1 = Thread(target=find_users_sync, args=(6,))
    th2 = Thread(target=find_users_sync, args=(2,))

    th3 = Thread(target=find_users_sync, args=(4,))

    th4 = Thread(target=find_users_sync, args=(5,))

    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()

    end = time.time()

    print(f'>>> 멀티쓰레드  처리 소요시간{ end-start }')
#print(f"Result: {sum(result)}")