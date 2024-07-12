import multiprocessing

# Define the function that will be executed by each process
def myFunc(i):
    print(f'calling myFunc from process n°: {i}')
    for j in range(i):
        print(f'output from myFunc is :{j}')


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


if __name__ == '__main__':
    
    print("\nRunning Scenario 2")
    scenario2()
    