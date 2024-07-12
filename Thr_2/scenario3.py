import threading
import time
import random

def function_A_random():
    time.sleep(random.uniform(1, 2))
    print(threading.current_thread().name + '--> random action A')

def function_B_random():
    time.sleep(random.uniform(1, 2))
    print(threading.current_thread().name + '--> random action B')

def function_C_random():
    time.sleep(random.uniform(1, 2))
    print(threading.current_thread().name + '--> random action C')


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
    
    run_scenario_3()
