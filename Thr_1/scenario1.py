import threading
import time
import random

def my_func_scenario_1(thread_number):
    print('Sequential: my_func called by thread N° {}'.format(thread_number))

def run_scenario_1():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func_scenario_1, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    print("Scenario 1: Sequential Execution with Modified Message")
    run_scenario_1()
    
