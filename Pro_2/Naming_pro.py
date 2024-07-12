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

def scenario_2():
    process_with_default_name_1 = multiprocessing.Process(target=myFunc_default_name)
    process_with_default_name_2 = multiprocessing.Process(target=myFunc_default_name)
    
    process_with_default_name_1.start()
    process_with_default_name_2.start()
    
    process_with_default_name_1.join()
    process_with_default_name_2.join()

def scenario_3():
    process_with_mixed_names = multiprocessing.Process(name='myFunc process', target=myFunc_custom_name)
    process_with_default_name_3 = multiprocessing.Process(target=myFunc_default_name)
    
    process_with_mixed_names.start()
    process_with_default_name_3.start()
    
    process_with_mixed_names.join()
    process_with_default_name_3.join()

if __name__ == '__main__':
    print("Running Scenario 1")
    scenario_1()
    print("\nRunning Scenario 2")
    scenario_2()
    
    print("\nRunning Scenario 3")
    scenario_3()