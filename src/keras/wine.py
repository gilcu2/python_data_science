import pandas as pd

if __name__ == "__main__":
    white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv",
                        sep=';')
    red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
                      sep=';')

    print(white.info())
    print(red.info())

    print(white.describe())
    print(red.describe())
