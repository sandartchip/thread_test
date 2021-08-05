import threading, time
players = ['ho','hu','hi']

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("subthread start", threading.currentThread().getName())
        time.sleep(10)
        print("subthread end", threading.currentThread().getName())


print("main thread start")
t1 = Worker("t1")
t1.start()

t2 = Worker("t2")
t2.start()
print("main thread end")


