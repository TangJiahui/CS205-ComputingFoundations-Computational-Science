import random
import multiprocessing
from multiprocessing import Pool


#caculate the number of points in the unit circle
#out of n points
def monte_carlo_pi_part(n):
    
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        
        # if it is within the unit circle
        if x*x + y*y <= 1:
            count = count + 1
        
    #return
    return count

if __name__=='__main__':
    
    np = multiprocessing.cpu_count()
    print('You have {0:1d} CPUs'.format(np))

    # Nummber of points to use for the Pi estimation
    #n = 100000000
    n = 10000000
    
    # iterable with a list of points to generate in each worker
    # each worker process gets n/np number of points to calculate Pi from

    part_count = [int(n/np) for i in range(np)]

    #Create the worker pool
    pool = Pool(processes=np)   

    # parallel map
    count = pool.map(monte_carlo_pi_part, part_count)

    print("Estimated value of Pi: {}".format(4.0 * sum(count) / n)) 
