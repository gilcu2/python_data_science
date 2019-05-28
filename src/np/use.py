import numpy as np

print(np.__version__)

int_vec=np.array([1, 4, 2, 5, 3])
print("int_vec: ",int_vec)

int_mat=np.array([range(i, i + 3) for i in [2, 4, 6]])
print("int_mat\n",int_mat)



