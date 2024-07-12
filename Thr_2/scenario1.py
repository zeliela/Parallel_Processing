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



if __name__ == "__main__":
    run_scenario_1()
   
