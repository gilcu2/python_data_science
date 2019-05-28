import numpy as np
import matplotlib.pyplot as plt
import seaborn

rand = np.random.RandomState(42)
mat = rand.rand(10, 2)

seaborn.set()
plt.scatter(mat[:, 0], mat[:, 1], s=100)