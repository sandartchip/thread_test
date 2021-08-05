import threading

def consumer(cond):
    name = threading.currentThread().getName()
    print('{} 시작'.format(name))

    with cond:
        print('{} 대기'.format(name))

        cond.wait()
        print('{} 자원 소비'.format(name))


def producer(cond):
    name = threading.currentThread().getName()
    print('{} 시작'.format(name))

    with cond:
        print('{} 자원 생산 후 모든 소비자에게 알림'.format(name))
        cond.notifyAll()


if __name__ == '__main__':
    condition = threading.Condition()

    consumer1 = threading.Thread(name='소비자1', target=consumer, args=(condition,))
    consumer2 = threading.Thread(name='소비자2', target=consumer, args=(condition,))

    producer1 = threading.Thread(name='생산자1', target=producer, args=(condition,))

    producer2 = threading.Thread(name='생산자2', target=producer, args=(condition,))
    producer3 = threading.Thread(name='생산자3', target=producer, args=(condition,))


    consumer1.start()
    consumer2.start()

    producer1.start()

    producer2.start()
    producer3.start()