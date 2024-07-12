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
        if self.scenario == 'new_locking_scenario':
            # New Locking Scenario
            threadLock.acquire()
            print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
            time.sleep(self.duration)
            print(f"---> {self.name} over")
            threadLock.release()

def run_new_locking_scenario():
    print("Running New Locking Scenario")
    start_time = time.time()
    threads = []

    for i in range(1, 10):
        thread = MyThreadClass(f"Thread#{i} ", randint(1, 10), 'new_locking_scenario')
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("New Locking Scenario End")
    # Execution Time
    print(f"--- New Locking Scenario: {time.time() - start_time} seconds ---\n")

if __name__ == "__main__":
    run_new_locking_scenario()
