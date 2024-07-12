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



def scenario_3():
    process_with_mixed_names = multiprocessing.Process(name='myFunc process', target=myFunc_custom_name)
    process_with_default_name_3 = multiprocessing.Process(target=myFunc_default_name)
    
    process_with_mixed_names.start()
    process_with_default_name_3.start()
    
    process_with_mixed_names.join()
    process_with_default_name_3.join()

if __name__ == '__main__':
    
    print("\nRunning Scenario 3")
    scenario_3()