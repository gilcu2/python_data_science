import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

import seaborn

rand = np.random.RandomState(42)
mat = rand.rand(10, 2)

seaborn.set()
plt.scatter(mat[:, 0], mat[:, 1], s=100)