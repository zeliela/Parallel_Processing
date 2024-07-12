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

def scenario1():
    # Scenario 1: Multiple Producers, Single Consumer
    t1 = threading.Thread(target=consumer_scenario1, args=(1,))
    t1.start()
    for i in range(1, 11):
        t2 = threading.Thread(target=producer_scenario1, args=(i,))
        t2.start()
        t2.join()
    t1.join()

def scenario2():
    # Scenario 2: Multiple Consumers, Single Producer
    t2 = threading.Thread(target=producer_scenario2, args=(1,))
    t2.start()
    for i in range(1, 11):
        t1 = threading.Thread(target=consumer_scenario2, args=(i,))
        t1.start()
        t1.join()
    t2.join()

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

# Main program
def main():
    logging.info("Running Scenario 1")
    scenario1()
    time.sleep(2)  # Delay between scenarios
    
    logging.info("Running Scenario 2")
    scenario2()
    time.sleep(2)  # Delay between scenarios
    
    logging.info("Running Scenario 3")
    scenario3()

if __name__ == "__main__":
    main()

