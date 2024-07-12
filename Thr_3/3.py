import threading
import time
import random
import os

class MyThread(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        print(f"---> Thread#{self.thread_id} running, belonging to process ID {os.getpid()}")
        time.sleep(random.uniform(1, 3))
        print(f"---> Thread#{self.thread_id} over")

class MyThreadFixedSleep(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        print(f"---> Thread#{self.thread_id} running, belonging to process ID {os.getpid()}")
        time.sleep(2)
        print(f"---> Thread#{self.thread_id} over")

class MyThreadIncreasingSleep(threading.Thread):
    def __init__(self, thread_id, sleep_time):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.sleep_time = sleep_time

    def run(self):
        print(f"---> Thread#{self.thread_id} running, belonging to process ID {os.getpid()}")
        time.sleep(self.sleep_time)
        print(f"---> Thread#{self.thread_id} over")

def run_scenario_1():
    print("Scenario 1: Ordered Start with Randomized Sleep")
    threads = []
    for i in range(1, 10):
        t = MyThread(i)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def run_scenario_2():
    print("\nScenario 2: Concurrent Start with Fixed Sleep")
    threads = []
    for i in range(1, 10):
        t = MyThreadFixedSleep(i)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def run_scenario_3():
    print("\nScenario 3: Sequential Start with Increasing Sleep Time")
    threads = []
    for i in range(1, 10):
        t = MyThreadIncreasingSleep(i, i)
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    start_time = time.time()
    run_scenario_1()
    run_scenario_2()
    run_scenario_3()
    print(f"End\n--- {time.time() - start_time} seconds ---")
