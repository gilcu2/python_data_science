from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    y = iris.target