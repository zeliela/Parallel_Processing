import threading
import time


# Scenario 2: Different arrival times
def race_participant_scenario2(name, barrier):
    print(f"{name} started racing!")
    time.sleep({"Dewey": 3, "Huey": 1, "Louie": 2}[name])  # Simulate different arrival times
    print(f"{name} reached the barrier at: {time.strftime('%a %b %d %H:%M:%S %Y')}")
    barrier.wait()


def run_race_scenario2():
    print("START RACE!!!!")
    barrier = threading.Barrier(3, action=lambda: print("Race over!"))
    names = ["Dewey", "Huey", "Louie"]
    threads = [threading.Thread(target=race_participant_scenario2, args=(name, barrier)) for name in names]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":

    print("\nScenario 2 Output:\n")
    run_race_scenario2()
    