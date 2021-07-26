
import socket
import random

HOST = 'localhost'

PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM ) as s:
    s.connect( (HOST, PORT) )

    #n = input("1-9 사이 숫자 입력")

    result_folder_id = random.randint(1, 9)

    send_txt = "JOB ID : " + str( result_folder_id ) # Folder ID 를 보냄

    s.sendall( send_txt.encode('utf-8') )

    received_data = s.recv(1024).decode('utf-8')
    # 서버로부터 데이터 받아 옴.

    print(f'서버 응답:{received_data}')
