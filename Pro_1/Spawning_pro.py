import multiprocessing

# Define the function that will be executed by each process
def myFunc(i):
    print(f'calling myFunc from process n°: {i}')
    for j in range(i):
        print(f'output from myFunc is :{j}')

# Scenario 1: Sequential Process Execution
def scenario1():
    print("Scenario 1: Sequential Process Execution")
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()  # Ensure each process completes before starting the next

# Scenario 2: Parallel Process Execution
def scenario2():
    print("Scenario 2: Parallel Process Execution")
    processes = []
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()  # Wait for all processes to complete

# Scenario 3: Staggered Process Execution
def scenario3():
    print("Scenario 3: Staggered Process Execution")
    processes = []
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        processes.append(process)
        process.start()
        if i % 2 == 0:  # Only join every second process immediately
            process.join()
    for process in processes:
        if process.is_alive():  # Join only the remaining processes that are still running
            process.join()

if __name__ == '__main__':
    print("Running Scenario 1")
    scenario1()
    print("\nRunning Scenario 2")
    scenario2()
    print("\nRunning Scenario 3")
    scenario3()
