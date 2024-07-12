import multiprocessing
import time

# Scenario 1: Default output
class MyProcess(multiprocessing.Process):
    def __init__(self):
        super().__init__()

    def run(self):
        print('called run method by %s' % self.name)

# Scenario 2: Printing additional information
class MyProcessWithInfo(multiprocessing.Process):
    def __init__(self):
        super().__init__()

    def run(self):
        print(f'called run method by {self.name} with PID {self.pid}')

# Scenario 3: Custom process names and additional message
class CustomNameProcess(multiprocessing.Process):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(f'called run method by {self.name} with custom message')

def scenario_1():
    print("Running Scenario 1")
    print("Scenario 1: Default output")
    for i in range(10):
        process = MyProcess()
        process.start()
        process.join()
    print("End of Scenario 1\n")

def scenario_2():
    print("Running Scenario 2")
    print("Scenario 2: Printing additional information")
    for i in range(10):
        process = MyProcessWithInfo()
        process.start()
        process.join()
    print("End of Scenario 2\n")

def scenario_3():
    print("Running Scenario 3")
    print("Scenario 3: Custom process names and additional message")
    for i in range(10):
        process = CustomNameProcess(name=f'CustomProcess-{i+1}')
        process.start()
        process.join()
    print("End of Scenario 3\n")

if __name__ == '__main__':
    scenario_1()
    scenario_2()
    scenario_3()
