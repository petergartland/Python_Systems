import time
import multiprocessing

def deposit(balance,lock):
	for i in range(1000):
		lock.acquire()
		val = balance.value
		val += 1
		time.sleep(.01)
		balance.value = val
		lock.release()
		
def withdraw(balance,lock):
	for i in range(1000):
		lock.acquire()
		val2 = balance.value
		val2 -= 1
		time.sleep(.01)
		balance.value = val2
		lock.release()
		
if __name__ == '__main__':
	balance = multiprocessing.Value('i', 200)
	lock = multiprocessing.Lock()
	d = multiprocessing.Process(target=deposit, args=(balance,lock))
	w = multiprocessing.Process(target=withdraw, args=(balance,lock))
	d.start()
	w.start()
	d.join()
	w.join()
	print(balance.value)
	
	
