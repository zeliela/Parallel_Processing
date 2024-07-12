import multiprocessing
import random
import time

class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f"Process Producer: item {item} appended to queue {self.name}")
            time.sleep(1)
            print(f"The size of queue is {self.queue.qsize()}")

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        
    def run(self):
        while True:
            if self.queue.empty():
                print("Process Consumer: the queue is empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print(f"Process Consumer: item {item} popped by {self.name}")
                time.sleep(1)



def scenario2():
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_consumer.sleep_time = 3  # Consumer waits longer
    
    process_producer.start()
    process_consumer.start()
    
    process_producer.join()
    process_consumer.join()



if __name__ == '__main__':

    scenario2()
    print("\nScenario 2 complete.\n")
    
