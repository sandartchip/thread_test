import asyncio
import time

async def find_users_sync(n):
    num=0
    for i in range(1, 1000000000):
        num += i
        #await asyncio.sleep(1)

    print(f'> 총 {num} 명 사용자 동기 조회 완료!')


async def process_sync():
    start =time.time()

    await find_users_sync(6)
    await find_users_sync(2)
    await find_users_sync(4)
    await find_users_sync(5)

    end = time.time()
    print(f'>>> 비동기 처리 소요시간{ end-start }')

if __name__ == '__main__':

    asyncio.run( process_sync() )



