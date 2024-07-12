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


# Scenario 2: Different Timing for Threads
def scenario_2():
    lock = threading.RLock()
    items_to_add = 16
    items_to_remove = 1
    items = []

    def add_items():
        nonlocal items_to_add
        while items_to_add > 0:
            with lock:
                items.append('item')
                items_to_add -= 1
                print(f"ADDED one item -->{items_to_add} item to ADD")
                time.sleep(0.05)  # Different sleep time

    def remove_items():
        nonlocal items_to_remove
        while items_to_remove > 0:
            with lock:
                if items and items_to_add <= 12:
                    items.pop()
                    items_to_remove -= 1
                    print(f"REMOVED one item -->{items_to_remove} item to REMOVE")
                    time.sleep(0.2)  # Different sleep time

    add_thread = threading.Thread(target=add_items)
    remove_thread = threading.Thread(target=remove_items)
    
    print(f"N° {items_to_add} items to ADD")
    print(f"N° {items_to_remove} items to REMOVE")
    
    add_thread.start()
    remove_thread.start()
    
    add_thread.join()
    remove_thread.join()


# Main function to run the scenarios
if __name__ == "__main__":

    print("\nScenario 2:")
    scenario_2()
   