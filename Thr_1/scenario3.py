import threading
import time
import random

def my_func_scenario_3(thread_number):
    delay = random.uniform(0.1, 1.0)
    time.sleep(delay)
    print(f'Immediate Concurrent: my_func called by thread N° {thread_number} with delay {delay:.2f}')

def run_scenario_3():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func_scenario_3, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    print("\nScenario 3: Immediate Concurrent Execution with Randomized Delay in Output")
    run_scenario_3()