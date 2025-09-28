import numpy as np
import time

size = 10_00_000

# python operation
py_list = list(range(size))
start = time.time()
py_result = [x * 2 for x in py_list]
end = time.time()
print("Python List Time:", end - start)

np_arr = np.arange(size)

# numpy operation
start = time.time()
np_result = np_arr * 2
end = time.time()
print("Numpy Array Time:", end - start)


x = np.array([1,2,3])
y = np.array([[10],[20],[30]])  

print("\nBroadcasting example:\n", x + y)
