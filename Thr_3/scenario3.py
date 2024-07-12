import threading
import time
import random
import os

class MyThreadIncreasingSleep(threading.Thread):
    def __init__(self, thread_id, sleep_time):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.sleep_time = sleep_time

    def run(self):
        print(f"---> Thread#{self.thread_id} running, belonging to process ID {os.getpid()}")
        time.sleep(self.sleep_time)
        print(f"---> Thread#{self.thread_id} over")


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
    run_scenario_3()
    print(f"End\n--- {time.time() - start_time} seconds ---")
