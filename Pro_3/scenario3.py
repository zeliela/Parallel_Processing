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

    print("Running Scenario 3")
    run_scenario3()
    print("\nScenario 3 completed.")
