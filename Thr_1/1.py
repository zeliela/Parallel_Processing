import threading
import time
import random

def my_func_scenario_1(thread_number):
    print('Sequential: my_func called by thread N° {}'.format(thread_number))

def my_func_scenario_2(thread_number):
    print('Concurrent Start: my_func called by thread N° {}'.format(thread_number))

def my_func_scenario_3(thread_number):
    time.sleep(random.uniform(0, 0.2))
    print('Random Delay: my_func called by thread N° {}'.format(thread_number))

def run_scenario_1():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func_scenario_1, args=(i,))
        threads.append(t)
        t.start()
        t.join()

def run_scenario_2():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func_scenario_2, args=(i,))
        threads.append(t)
        t.start()
        time.sleep(0.1)

    for t in threads:
        t.join()

def run_scenario_3():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func_scenario_3, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    print("Scenario 1: Sequential Execution with Modified Message")
    run_scenario_1()
    print("\nScenario 2: Concurrent Execution with Delayed Start and Unique Messages")
    run_scenario_2()
    print("\nScenario 3: Immediate Concurrent Execution with Randomized Delay in Output")
    run_scenario_3()
