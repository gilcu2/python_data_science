import seaborn as sns
sns.set()
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data_name = "iris"
    target_var = "species"

    data=sns.load_dataset(data_name)
    (X, y) =(data.drop(target_var,axis=1),data[target_var])

    model = GaussianMixture(n_components=3, covariance_type='full')
    model.fit(X)

    y_gmm = model.predict(X)

    # Need the PCA to show
    # data['cluster'] = y_gmm
    # sns.lmplot("PCA1", "PCA2", data=data, hue='species',
    #            col='cluster', fit_reg=False)
    # plt.show()