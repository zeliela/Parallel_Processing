import threading
import time
import os
from threading import Thread
from random import randint

threadLock = threading.Lock()

class MyThreadClass(Thread):
    def __init__(self, name, duration, scenario):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
        self.scenario = scenario

    def run(self):
        if self.scenario == 'sequential':
            # Sequential Execution with Locking
            threadLock.acquire()
            try:
                print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
            finally:
                threadLock.release()
            time.sleep(self.duration)
            print(f"---> {self.name} over")

def run_sequential():
    print("Running Sequential Scenario")
    start_time = time.time()
    threads = []

    for i in range(1, 10):
        thread = MyThreadClass(f"Thread#{i} ", randint(1, 10), 'sequential')
        threads.append(thread)

    for thread in threads:
        thread.start()

    
    for thread in threads:
        thread.join()

    
    print("Sequential End")
    # Execution Time
    print(f"--- Sequential Scenario: {time.time() - start_time} seconds ---\n")

if __name__ == "__main__":
    run_sequential()
