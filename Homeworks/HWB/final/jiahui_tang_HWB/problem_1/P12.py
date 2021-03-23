import numpy as np
import multiprocessing as mp
import time
import matplotlib.pyplot as plt

# Sleep for t seconds
def burnTime(t):
	time.sleep(t)

# Main
if __name__ == '__main__':
	N = 16 # The number of jobs
	P = 4  # The number of processes

	# A thread pool of P processes
	pool = mp.Pool(P)

  # Use a variety of wait times
	ratio = []
	wait_time = [1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1,10,100]

	for t in wait_time:
		# Compute jobs serially and in parallel (you have to write this code)
		# Use time.time() to compute the elapsed time for each
		# serially
		sstart = time.time()
		for n in range(N):
			burnTime(t)
		send = time.time()
		serialTime = send-sstart
		print(serialTime)
		
		# parallels
		pstart = time.time()
		
		# iterable with a list of points to generate in each process
		part_count = [t] * N
		pool.map(burnTime, part_count)
		pend = time.time()	
		parallelTime = pend-pstart
		print(parallelTime)

		# Compute the ratio of these times
		ratio.append(serialTime/parallelTime)

	# Plot the results
	plt.plot(wait_time, ratio, '-ob')
	plt.xscale('log')
	plt.xlabel('Wait Time (sec)')
	plt.ylabel('Serial Time (sec) / Parallel Time (sec)')
	plt.title('Speedup versus function time')
	plt.show()
