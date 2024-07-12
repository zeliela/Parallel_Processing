import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
semaphore = threading.Semaphore(0)
item = 0
lock = threading.Lock()

def consumer_scenario3(i):
    threading.current_thread().name = f'Thread-{i * 2 - 1}'
    logging.info('Consumer is waiting')
    semaphore.acquire()
    with lock:
        logging.info('Consumer notify: item number {}'.format(item))

def producer_scenario3(i):
    threading.current_thread().name = f'Thread-{i * 2}'
    global item
    time.sleep(3)
    with lock:
        item = random.randint(0, 1000)
        logging.info('Producer notify: item number {}'.format(item))
    semaphore.release()

def scenario3():
    # Scenario 3: Multiple Producers, Multiple Consumers
    consumers = []
    producers = []
    
    for i in range(1, 11):
        t1 = threading.Thread(target=consumer_scenario3, args=(i,))
        t2 = threading.Thread(target=producer_scenario3, args=(i,))
        consumers.append(t1)
        producers.append(t2)
        t1.start()
        t2.start()
    
    for t1 in consumers:
        t1.join()
    for t2 in producers:
        t2.join()

if __name__ == "__main__":
    logging.info("Running Scenario 3")
    scenario3()
