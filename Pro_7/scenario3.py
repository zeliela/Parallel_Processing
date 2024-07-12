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
   
    print("\nRunning Scenario 3")
    scenario3()
