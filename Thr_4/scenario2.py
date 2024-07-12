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
        if self.scenario == 'concurrent':
            # Concurrent Execution without Locking
            print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
            time.sleep(self.duration)
            print(f"---> {self.name} over")

def run_concurrent():
    print("Running Concurrent Scenario")
    start_time = time.time()
    threads = []

    for i in range(1, 10):
        thread = MyThreadClass(f"Thread#{i} ", randint(1, 10), 'concurrent')
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    
    print("Concurrent End")
    # Execution Time
    print(f"--- Concurrent Scenario: {time.time() - start_time} seconds ---\n")

if __name__ == "__main__":
    run_concurrent()
