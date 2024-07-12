import multiprocessing
import time

def myFunc_custom_name():
    name = multiprocessing.current_process().name
    print("Starting process name = %s \n" % name)
    time.sleep(3)
    print("Exiting process name = %s \n" % name)

def myFunc_default_name():
    name = multiprocessing.current_process().name
    print("Starting process name = %s \n" % name)
    time.sleep(3)
    print("Exiting process name = %s \n" % name)

def scenario_1():
    process_with_name_1 = multiprocessing.Process(name='myFunc process', target=myFunc_custom_name)
    process_with_name_2 = multiprocessing.Process(name='Process-2', target=myFunc_custom_name)
    
    process_with_name_1.start()
    process_with_name_2.start()
    
    process_with_name_1.join()
    process_with_name_2.join()

if __name__ == '__main__':
    print("Running Scenario 1")
    scenario_1()
   