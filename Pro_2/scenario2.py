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


def scenario_2():
    process_with_default_name_1 = multiprocessing.Process(target=myFunc_default_name)
    process_with_default_name_2 = multiprocessing.Process(target=myFunc_default_name)
    
    process_with_default_name_1.start()
    process_with_default_name_2.start()
    
    process_with_default_name_1.join()
    process_with_default_name_2.join()



if __name__ == '__main__':

    print("\nRunning Scenario 2")
    scenario_2()
  