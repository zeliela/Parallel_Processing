import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
semaphore = threading.Semaphore(0)
item = 0
lock = threading.Lock()

def consumer_scenario1(i):
    threading.current_thread().name = f'Thread-{i * 2 - 1}'
    logging.info('Consumer is waiting')
    semaphore.acquire()
    with lock:
        logging.info('Consumer notify: item number {}'.format(item))

def producer_scenario1(i):
    threading.current_thread().name = f'Thread-{i * 2}'
    global item
    time.sleep(3)
    with lock:
        item = random.randint(0, 1000)
        logging.info('Producer notify: item number {}'.format(item))
    semaphore.release()

def scenario1():
    # Scenario 1: Multiple Producers, Single Consumer
    t1 = threading.Thread(target=consumer_scenario1, args=(1,))
    t1.start()
    for i in range(1, 11):
        t2 = threading.Thread(target=producer_scenario1, args=(i,))
        t2.start()
        t2.join()
    t1.join()

if __name__ == "__main__":
    logging.info("Running Scenario 1")
    scenario1()
