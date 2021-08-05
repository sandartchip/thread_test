
import time

def sleep():
    time.sleep(1)

def sum(name, numbers):
    start = time.time()
    total = 0
    for number in numbers:
        sleep()
        total += number
        print(f'작업중={name}, number={number}, total={total}')
    end = time.time()
    print(f'작업명={name}, 걸린 시간={end-start}')
    return total

def main():
    start = time.time()

    result1 = sum("A 루틴", [1, 2])
    result2 = sum("B 루틴", [1, 2, 3])

    end = time.time()
    print(f'총합={result1+result2}, 총 !!시간={end-start}')

if __name__ == "__main__":
    main()