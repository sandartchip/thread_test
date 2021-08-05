import time

def find_users_sync(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        time.sleep(1)
    print(f'> 총 {n} 명 사용자 동기 조회 완료!')

def process_sync():
    start = time.time()

    find_users_sync(6)
    find_users_sync(2)
    find_users_sync(4)
    find_users_sync(5)

    end = time.time()
    print(f'>>> 동기 처리 총 소요 시간: {end - start}')

if __name__ == '__main__':
    process_sync()