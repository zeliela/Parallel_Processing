import multiprocessing
from multiprocessing import Queue

# Define the function that will be executed by each process
def myFunc(i, queue):
    output = []
    output.append(f'calling myFunc from process n°: {i}')
    for j in range(i):
        output.append(f'output from myFunc is :{j}')
    queue.put(output)

# Scenario 1: Sequential Process Execution
def scenario1():
    print("Scenario 1: Sequential Process Execution")
    results_queue = Queue()
    statements = []

    processes = []

    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i, results_queue))
        processes.append(process)
        process.start()
        process.join()  # Ensure each process completes before starting the next

    # Collect results from queue
    while not results_queue.empty():
        statements.extend(results_queue.get())

    return statements, "Scenario 1: Sequential Process Execution"

if __name__ == '__main__':
    results, scenario_desc = scenario1()
    for line in results:
        print(line)
