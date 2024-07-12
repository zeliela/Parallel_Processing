import threading
import time
import random

def function_A():
    print(threading.current_thread().name + '--> starting')
    time.sleep(2)
    print(threading.current_thread().name + '--> exiting')

def function_B():
    print(threading.current_thread().name + '--> starting')
    time.sleep(2)
    print(threading.current_thread().name + '--> exiting')

def function_C():
    print(threading.current_thread().name + '--> starting')
    time.sleep(2)
    print(threading.current_thread().name + '--> exiting')

def function_A_diff_sleep():
    print(threading.current_thread().name + '--> starting')
    time.sleep(1)
    print(threading.current_thread().name + '--> exiting')

def function_B_diff_sleep():
    print(threading.current_thread().name + '--> starting')
    time.sleep(2)
    print(threading.current_thread().name + '--> exiting')

def function_C_diff_sleep():
    print(threading.current_thread().name + '--> starting')
    time.sleep(3)
    print(threading.current_thread().name + '--> exiting')

def function_A_random():
    time.sleep(random.uniform(1, 2))
    print(threading.current_thread().name + '--> random action A')

def function_B_random():
    time.sleep(random.uniform(1, 2))
    print(threading.current_thread().name + '--> random action B')

def function_C_random():
    time.sleep(random.uniform(1, 2))
    print(threading.current_thread().name + '--> random action C')

def run_scenario_1():
    print("Scenario 1: Sequential Execution with Modified Message")
    t1 = threading.Thread(name='function_A_Seq', target=function_A)
    t1.start()
    t1.join()

    t2 = threading.Thread(name='function_B_Seq', target=function_B)
    t2.start()
    t2.join()

    t3 = threading.Thread(name='function_C_Seq', target=function_C)
    t3.start()
    t3.join()

def run_scenario_2():
    print("\nScenario 2: Concurrent Execution with Different Sleep Times")
    t1 = threading.Thread(name='function_A_DiffSleep', target=function_A_diff_sleep)
    t2 = threading.Thread(name='function_B_DiffSleep', target=function_B_diff_sleep)
    t3 = threading.Thread(name='function_C_DiffSleep', target=function_C_diff_sleep)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

def run_scenario_3():
    print("\nScenario 3: Immediate Concurrent Execution with Randomized Output Message")
    t1 = threading.Thread(name='function_A_Random', target=function_A_random)
    t2 = threading.Thread(name='function_B_Random', target=function_B_random)
    t3 = threading.Thread(name='function_C_Random', target=function_C_random)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    run_scenario_1()
    run_scenario_2()
    run_scenario_3()
