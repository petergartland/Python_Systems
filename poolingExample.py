from multiprocessing import Pool
import time

def f(n):
	sum = 0
	for x in range (1000):
		sum += x*2
	return sum
	
if __name__ == '__main__':
	t1 = time.time()
	p = Pool(processes=3)
	results = p.map(f,range(10000))
	p.close()
	p.join()
	print("pool took", time.time()-t1)
	
	result	= []
	t2 = time.time()	
	for x in range(10000):
		result.append(f(x))
	print("result of serial took", time.time() - t2)

