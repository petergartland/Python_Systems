import time
import multiprocessing


def calc_square(numbers, results, v, q):
	v.value = 5.5
	for index, i in enumerate(numbers):
		print('square: ',i**2)
		results[index] = (i**2)
		q.put(i**2)
	print('inside process results:', results[:])
			

if __name__ == "__main__":
	
	array = [2,3,8,9]
	results = multiprocessing.Array('i',4)
	v = multiprocessing.Value('d', 0.0)
	q = multiprocessing.Queue()
	t1 = multiprocessing.Process(target=calc_square, args=(array,results,v,q))
	t1.start()
	t1.join()
	print('outside process results:', results[:])
	print('value outside process:', v.value)
	while(q.empty() == False):
		print('value of queue outside process:',q.get())
