import multiprocessing
import time
import os
import signal

def foo():
    print('Starting function')
    for i in range(0, 10):
        print('-->%d\n' % i)
        time.sleep(1)
    print('Finished function')

def scenario_1():
    print("Scenario 1")
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    p.terminate()
    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
    print()

def scenario_2():
    print("Scenario 2")
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    time.sleep(2)  # Allow the process to run for a while
    os.kill(p.pid, signal.SIGTERM)  # Send SIGTERM signal to the process
    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
    print()

def scenario_3():
    print("Scenario 3")
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    p.join(1)  # Join with a timeout of 1 second
    if p.is_alive():
        print('Process is still running, terminating now...')
        p.terminate()
    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
    print()

if __name__ == '__main__':
    print("Running Scenario 1")
    scenario_1()
    print("Running Scenario 2")
    scenario_2()
    print("Running Scenario 3")
    scenario_3()
