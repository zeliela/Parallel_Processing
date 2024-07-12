import threading
import time
import random


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



if __name__ == "__main__":
    run_scenario_2()
   
