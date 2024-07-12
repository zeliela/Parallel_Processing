import threading
import time

# Scenario 1: Different arrival times
def race_participant_scenario1(name, barrier):
    print(f"{name} started racing!")
    time.sleep({"Dewey": 1, "Huey": 2, "Louie": 3}[name])  # Simulate different arrival times
    print(f"{name} reached the barrier at: {time.strftime('%a %b %d %H:%M:%S %Y')}")
    barrier.wait()

def run_race_scenario1():
    print("START RACE!!!!")
    barrier = threading.Barrier(3, action=lambda: print("Race over!"))
    names = ["Dewey", "Huey", "Louie"]
    threads = [threading.Thread(target=race_participant_scenario1, args=(name, barrier)) for name in names]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()



if __name__ == "__main__":
    print("\nScenario 1 Output:\n")
    run_race_scenario1()
  