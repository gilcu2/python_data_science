import seaborn as sns
sns.set()
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data_name = "iris"
    target_var = "species"

    data=sns.load_dataset(data_name)
    (X, y) =(data.drop(target_var,axis=1),data[target_var])

    model = PCA(n_components=2)
    model.fit(X)

    X_2D = model.transform(X)

    data['PCA1'] = X_2D[:, 0]
    data['PCA2'] = X_2D[:, 1]
    sns.lmplot("PCA1", "PCA2", hue='species', data=data, fit_reg=False)
    plt.show()