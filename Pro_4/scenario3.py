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

    print("Running Scenario 3")
    scenario_3()
