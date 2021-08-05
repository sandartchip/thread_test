import asyncio
import random

async def tcp_echo_client(message):
    #reader, writer = await asyncio.open_connection(
    #    '127.0.0.1', 8888)

    reader, writer = await asyncio.open_connection(
        '219.240.45.234', 8888)

    # 비동기 커넥션을 열고 주소, 포트 번호 지정 후
    # 서버로부터의 결과 저장할 writer 객체 지정

    print(f'Send: {message!r}') # 보낼 메시지 확인
    writer.write( message.encode() ) # 메세지를 인코드하여 서버로 메세지 send.

    returned_data  = await reader.read(100)
    # 서버로부터 응답 결과 리턴 받음을 때까지 대기.
    # 받고 난 후 after_analyze 화면으로 전환
    print(f'Received: {returned_data.decode()!r}')

    print('Close the connection')
    writer.close()

if __name__ =="__main__":
    folder_id = random.randint(1, 9)
    asyncio.run(tcp_echo_client(  str(folder_id) ))