import threading
import time
import os
from threading import Thread
from random import randint

threadLock = threading.Lock()

class MyThreadClass(Thread):
    def __init__(self, name, scenario):
        Thread.__init__(self)
        self.name = name
        self.scenario = scenario

    def run(self):
        if self.scenario == 'delay':
            delay = randint(1, 5)
            threadLock.acquire()
            try:
                print(f"---> {self.name} starting, belonging to process ID {os.getpid()}")
            finally:
                threadLock.release()
            time.sleep(delay)
            threadLock.acquire()
            try:
                print(f"---> {self.name} finished after {delay} seconds")
            finally:
                threadLock.release()

def run_delay_scenario():
    print("Running Delay Scenario")
    start_time = time.time()
    threads = []

    for i in range(1, 11):
        thread = MyThreadClass(f"Thread#{i}", 'delay')
        threads.append(thread)

    for i in range(0, len(threads), 2):
        threads[i].start()
        if i + 1 < len(threads):
            threads[i + 1].start()

        threads[i].join()
        if i + 1 < len(threads):
            threads[i + 1].join()

    print("Delay Scenario End")
    
    print(f"--- Delay Scenario: {time.time() - start_time} seconds ---\n")

if __name__ == "__main__":
    run_delay_scenario()
