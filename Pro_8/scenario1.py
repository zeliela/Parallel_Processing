import multiprocessing

# Function to square a number
def function_square(data):
    return data * data


def scenario_square():
    inputs = list(range(0, 101))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    print('Scenario 1 - Squaring numbers:')
    print('Pool :', pool_outputs)


if __name__ == '__main__':
    scenario_square()
    
