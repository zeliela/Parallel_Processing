import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
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
        elif self.scenario == 'concurrent':
            # Concurrent Execution without Locking
            print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
            time.sleep(self.duration)
            print(f"---> {self.name} over")
        elif self.scenario == 'new_locking_scenario':
            # New Locking Scenario
            threadLock.acquire()
            print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
            time.sleep(self.duration)
            print(f"---> {self.name} over")
            threadLock.release()

def run_scenario(scenario):
    start_time = time.time()
    threads = []

    # Thread Creation
    for i in range(1, 10):
        thread = MyThreadClass(f"Thread#{i} ", randint(1, 10), scenario)
        threads.append(thread)

    if scenario == 'new_locking_scenario':
        # Thread Running
        for thread in threads:
            thread.start()

        # Thread Joining
        for thread in threads:
            thread.join()
    else:
        # Thread Running
        for thread in threads:
            thread.start()

        # Thread Joining
        for thread in threads:
            thread.join()

    # End
    print(f"{scenario.capitalize()} End")
    # Execution Time
    print(f"--- {scenario.capitalize()} Scenario: {time.time() - start_time} seconds ---\n")

def main():
    run_scenario('sequential')  # This should produce the primary output
    run_scenario('concurrent')
    run_scenario('new_locking_scenario')

if __name__ == "__main__":
    main()

