import multiprocessing

# Function to double a number
def function_double(data):
    return data * 2

def scenario_double():
    inputs = list(range(0, 51))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_double, inputs)
    pool.close()
    pool.join()
    print('\nScenario 3 - Doubling numbers:')
    print('Pool :', pool_outputs)

if __name__ == '__main__':
    
    scenario_double()
