import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time, sleep
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))

def scenario1():
    synchronizer = Barrier(2)
    serializer = Lock()
    processes = [
        Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)),
        Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)),
        Process(name='p3 - test_without_barrier', target=test_without_barrier),
        Process(name='p4 - test_without_barrier', target=test_without_barrier)
    ]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

def scenario2():
    synchronizer = Barrier(3)
    serializer = Lock()
    processes = [
        Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)),
        Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)),
        Process(name='p3 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)),
        Process(name='p4 - test_without_barrier', target=test_without_barrier)
    ]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

def scenario3():
    synchronizer = Barrier(2)
    serializer = Lock()
    processes = [
        Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)),
        Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)),
        Process(name='p3 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)),
        Process(name='p4 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer))
    ]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

if __name__ == '__main__':
    print("Running Scenario 1")
    scenario1()
    
    
