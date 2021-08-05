import time
import concurrent.futures

def func1():
    while True:
        print("func1")
        time.sleep(1)


def func2():

    while True:
        print("func2")
        time.sleep(1)

def find_users_sync(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        time.sleep(1)
    print(f'> 총 {n} 명 사용자 동기 조회 완료!')


if __name__ == "__main__":
    start = time.time()

    pool = concurrent.futures.ThreadPoolExecutor(max_workers = 3)

    future1 = pool.submit( find_users_sync, 3) # 함수명, 파라미터
    future2 = pool.submit( find_users_sync, 5) # 함수명, 파라미터

    future1.done()
    future2.done()



    end = time.time()
<<<<<<< HEAD
    print(f'>>> 비동기 처리 소요시간{ end-start }')
=======
    print(f'>>> 비동기 처리 소요시간{ end-start }')
>>>>>>> ebbaa7dad79e364bfa499c2214dc13f21c28e7ae
