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

# Scenario 1: Exact Primary Output
def scenario_1():
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
                time.sleep(0.1)

    def remove_items():
        nonlocal items_to_remove
        while items_to_remove > 0:
            with lock:
                if items and items_to_add <= 3:
                    items.pop()
                    items_to_remove -= 1
                    print(f"REMOVED one item -->{items_to_remove} item to REMOVE")
                    time.sleep(0.1)

    add_thread = threading.Thread(target=add_items)
    remove_thread = threading.Thread(target=remove_items)
    
    print(f"N° {items_to_add} items to ADD")
    print(f"N° {items_to_remove} items to REMOVE")
    
    add_thread.start()
    remove_thread.start()
    
    add_thread.join()
    remove_thread.join()


if __name__ == "__main__":
    print("Scenario 1:")
    scenario_1()
   