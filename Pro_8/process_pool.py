import multiprocessing

# Function to square a number
def function_square(data):
    return data * data

# Function to cube a number
def function_cube(data):
    return data * data * data

# Function to double a number
def function_double(data):
    return data * 2

def scenario_square():
    inputs = list(range(0, 101))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    print('Scenario 1 - Squaring numbers:')
    print('Pool :', pool_outputs)

def scenario_cube():
    inputs = list(range(0, 34))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_cube, inputs)
    pool.close()
    pool.join()
    print('\nScenario 2 - Cubing numbers:')
    print('Pool :', pool_outputs)

def scenario_double():
    inputs = list(range(0, 51))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_double, inputs)
    pool.close()
    pool.join()
    print('\nScenario 3 - Doubling numbers:')
    print('Pool :', pool_outputs)

if __name__ == '__main__':
    scenario_square()
    scenario_cube()
    scenario_double()
