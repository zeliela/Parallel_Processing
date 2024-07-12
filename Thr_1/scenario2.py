import threading
import time
import random

def my_func_scenario_2(thread_number):
    print('Concurrent Start: my_func called by thread N° {}'.format(thread_number))

def run_scenario_2():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func_scenario_2, args=(i,))
        threads.append(t)
        t.start()
        time.sleep(0.1)

    for t in threads:
        t.join()



if __name__ == "__main__":
   
    print("\nScenario 2: Concurrent Execution with Delayed Start and Unique Messages")
    run_scenario_2()
    