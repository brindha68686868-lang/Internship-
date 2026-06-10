from multiprocessing import Process
import time

def worker(name):
    for i in range(5):
        print(f"{name}: {i + 1}")
        time.sleep(1)

if __name__ == "__main__":
    p1 = Process(target=worker, args=("Process-1",))
    p2 = Process(target=worker, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes completed!")