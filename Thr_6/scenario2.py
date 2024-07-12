import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
semaphore = threading.Semaphore(0)
item = 0

def consumer_scenario2(i):
    threading.current_thread().name = f'Thread-{i * 2 - 1}'
    logging.info('Consumer is waiting')
    semaphore.acquire()
    logging.info('Consumer notify: item number {}'.format(item))

def producer_scenario2(i):
    threading.current_thread().name = f'Thread-{i * 2}'
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('Producer notify: item number {}'.format(item))
    for _ in range(10):  # Release semaphore for all consumers
        semaphore.release()

def scenario2():
    # Scenario 2: Multiple Consumers, Single Producer
    t2 = threading.Thread(target=producer_scenario2, args=(1,))
    t2.start()
    for i in range(1, 11):
        t1 = threading.Thread(target=consumer_scenario2, args=(i,))
        t1.start()
        t1.join()
    t2.join()

if __name__ == "__main__":
    logging.info("Running Scenario 2")
    scenario2()
