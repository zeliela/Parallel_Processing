import threading
import time

# Scenario 3: Equal arrival times
def race_participant_scenario3(name, barrier):
    print(f"{name} started racing!")
    time.sleep(2)  # All reach the barrier at the same time
    print(f"{name} reached the barrier at: {time.strftime('%a %b %d %H:%M:%S %Y')}")
    barrier.wait()

def run_race_scenario3():
    print("START RACE!!!!")
    barrier = threading.Barrier(3, action=lambda: print("Race over!"))
    names = ["Dewey", "Huey", "Louie"]
    threads = [threading.Thread(target=race_participant_scenario3, args=(name, barrier)) for name in names]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":

    print("\nScenario 3 Output:\n")
    run_race_scenario3()