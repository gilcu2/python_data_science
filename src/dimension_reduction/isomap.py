from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap

if __name__ == '__main__':
    digits = load_digits()

    X = digits.data
    y = digits.target

    iso = Isomap(n_components=2)
    iso.fit(digits.data)
    data_projected = iso.transform(digits.data)
    print(data_projected.shape)

    plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target,
                edgecolor='none', alpha=0.5,
                cmap=plt.cm.get_cmap('Spectral', 10))
    plt.colorbar(label='digit label', ticks=range(10))
    plt.clim(-0.5, 9.5)
    plt.show()

