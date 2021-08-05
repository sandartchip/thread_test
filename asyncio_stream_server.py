import asyncio
import pymysql

async def connect_db_fetch_data( folder_id ):
    sero_db_conn = pymysql.connect(
        user='root',
        passwd='1234',
        #host='127.0.0.1',
        host= 'apple.snu.ac.kr',
        db='soyeon_pj',
        port=3308,
        charset='utf8'
    )

    cursor = sero_db_conn.cursor(pymysql.cursors.DictCursor)

    folder_id = str( 189 + int(folder_id)  )# 로 가지고 오거나 아니면 Folder name 외래키 참조로 .

    query = "SELECT * FROM soyeon_pj_job WHERE result_folder_id=%s"

    #query = "SELECT * FROM `soyeon_pj_job`"

    cursor.execute(query, (folder_id))

    result = cursor.fetchall() # 데이터 패치

    print("-----------------------출력 시작-----------", folder_id)

    for r in result:
        print (r['id'], r['depth'], r['phred_quality'], r['evalue'], r['identity'], r['coverage'], r['result_folder_id'])
    # os.cmd(f"python main.py -c {coverage} ")

    await asyncio.sleep(2)
    print("-----------------------출력 끝-----------", folder_id)

    sero_db_conn.close()

async def handle_request(reader, writer): #  클라이언트로부터 새로운 요청 들어오면 처리하는 핸들러 함수.

    # reader, writer를 매개변수로 받아 옴.

    data = await reader.read(100) # reader로부터 100byte(?) 읽어 온다.

    message = data.decode() # 받아온 데이터를 디코드 함.

    addr = writer.get_extra_info('peername') # 클라이언트 주소 알아 옴

    '''
        클라이언트로부터 받은 folder id 값 읽기  
    '''

    print(f"Received {message!r} from {addr!r}")

    new_task = asyncio.create_task( connect_db_fetch_data(message)) # 태스크 객체 생성.
    await new_task

    print(f"Send to 클라이언트 : {message!r}")
    writer.write(data)
    await writer.drain() # ???

    print(f"Close the connection: {message}")
    print(f"===========END OF CONNECTION===================={message}")
    writer.close()

async def main():

    server = await asyncio.start_server( handle_request, '127.0.0.1', 8888 )

    server_addr = server.sockets[0].getsockname()

    print(f'Serving on {server_addr}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    #connect_db()
    asyncio.run( main() )
    # run() 함수는 전달된 코루틴을 실행하고, asyncio 이벤트 루프와 비동기 제너레이터의 파이널리제이션과 쓰레드 풀 닫기를 관리함.
    # run() 함수는 항상 새 이벤트 루프를 만들고, 끝에 이벤트 루프를 닫음.
    # asyncio 프로그램의 메인 진입 지점으로 사용해야 하고, 이상적으로는 한 번만 호출해야 한다.



