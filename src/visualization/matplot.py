import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.show()