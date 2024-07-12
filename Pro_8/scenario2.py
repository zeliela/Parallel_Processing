import multiprocessing


# Function to cube a number
def function_cube(data):
    return data * data * data



def scenario_cube():
    inputs = list(range(0, 34))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_cube, inputs)
    pool.close()
    pool.join()
    print('\nScenario 2 - Cubing numbers:')
    print('Pool :', pool_outputs)



if __name__ == '__main__':
   
    scenario_cube()
    
