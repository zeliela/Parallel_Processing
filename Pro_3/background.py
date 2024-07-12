import multiprocessing
import time

def foo(name):
    print(f"Starting {name}")
    if name == 'background_process':
        for i in range(0, 5):
            print(f'---> {i}')
            time.sleep(1)
    elif name == 'NO_background_process':
        for i in range(5, 10):
            print(f'---> {i}')
            time.sleep(1)
    print(f"Exiting {name}")

def run_scenario1():
    # Scenario 1: The desired primary output
    NO_background_process1 = multiprocessing.Process(name='NO_background_process', target=foo, args=('NO_background_process',))
    background_process = multiprocessing.Process(name='background_process', target=foo, args=('background_process',))
    NO_background_process2 = multiprocessing.Process(name='NO_background_process', target=foo, args=('NO_background_process',))
    
    NO_background_process1.start()
    NO_background_process1.join()

    NO_background_process2.start()
    background_process.start()

    NO_background_process2.join()
    background_process.join()

def run_scenario2():
    # Scenario 2: Running both processes in parallel with different daemon settings
    background_process = multiprocessing.Process(name='background_process', target=foo, args=('background_process',))
    background_process.daemon = True
    
    NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo, args=('NO_background_process',))
    NO_background_process.daemon = False
    
    NO_background_process.start()
    background_process.start()
    
    NO_background_process.join()
    background_process.join()

def run_scenario3():
    # Scenario 3: Different daemon settings affecting termination behavior
    background_process = multiprocessing.Process(name='background_process', target=foo, args=('background_process',))
    background_process.daemon = True
    
    NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo, args=('NO_background_process',))
    NO_background_process.daemon = True
    
    background_process.start()
    NO_background_process.start()
    
    background_process.join()
    NO_background_process.join()

if __name__ == '__main__':
    print("Running Scenario 1")
    run_scenario1()
    print("\nScenario 1 completed.\n\n")
    
    print("Running Scenario 2")
    run_scenario2()
    print("\nScenario 2 completed.\n\n")
    
    print("Running Scenario 3")
    run_scenario3()
    print("\nScenario 3 completed.")
