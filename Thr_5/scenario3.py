import threading
import time
import random

# Box class with RLock for thread-safe add and remove operations
class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

# Adder function for adding items
def adder(box, items):
    print("N° {} items to ADD \n".format(items))
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print("ADDED one item -->{} item to ADD \n".format(items))

# Remover function for removing items
def remover(box, items):
    print("N° {} items to REMOVE\n".format(items))
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print("REMOVED one item -->{} item to REMOVE\n".format(items))


# Scenario 3: Using Box Class Implementation
def scenario_3():
    items_to_add = 16
    items_to_remove = 1
    box = Box()

    t1 = threading.Thread(target=adder, args=(box, items_to_add))
    t2 = threading.Thread(target=remover, args=(box, items_to_remove))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

# Main function to run the scenarios
if __name__ == "__main__":

    print("\nScenario 3:")
    scenario_3()