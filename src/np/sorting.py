import numpy as np
from numpy.core._multiarray_umath import ndarray

vector: ndarray = np.array([2, 1, 4, 3, 5])
print("vector: ", vector)

vector.sort()
print("sorted: ", vector)

vector_partitioned=np.partition(vector, 2)
print("partitioned: ", vector_partitioned)

rand = np.random.RandomState(42)
matrix: ndarray = rand.randint(0, 10, (4, 6))
print("Matrix:\n", matrix)

X_sorted_by_column=np.sort(matrix, axis=0)
print("sorted by columns:\n",X_sorted_by_column)