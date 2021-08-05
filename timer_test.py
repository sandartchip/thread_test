from time import sleep
from timer import RepeatedTimer

def hello(name):
    print ("Hello %s!" % name)

print ("starting...")


if __name__ == "__main__":
    rt = RepeatedTimer(3, hello, "World")

    try:


    finally:
        rt.stop()