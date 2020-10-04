import time
import multiprocessing

def calc_square(numbers):
	for i in numbers:
		time.sleep(.2)
		print('square: ',i**2)
			
def calc_cube(numbers):
	for i in numbers:
		time.sleep(.2)
		print('cube: ', i**3)
			

if __name__ == "__main__":
	
	array = [2,3,8,9]
	t = time.time()

	t1 = multiprocessing.Process(target=calc_square, args=(array,))
	t2 = multiprocessing.Process(target=calc_cube, args=(array,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()
	#calc_square(array)
	#calc_cube(array)

	print("I finished in time ", time.time()-t)
