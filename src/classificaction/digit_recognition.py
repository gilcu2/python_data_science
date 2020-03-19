from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns


if __name__ == '__main__':
    digits = load_digits()
    print(digits.images.shape)

    # Visualization
    # fig, axes = plt.subplots(10, 10, figsize=(8, 8),
    #                          subplot_kw={'xticks': [], 'yticks': []},
    #                          gridspec_kw=dict(hspace=0.1, wspace=0.1))
    # for i, ax in enumerate(axes.flat):
    #     ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
    #     ax.text(0.05, 0.05, str(digits.target[i]), transform=ax.transAxes, color='green')
    #
    # plt.show()

    X = digits.data
    y = digits.target

    print(f"X shape: {X.shape} y shape {y.shape}")

    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

    model = GaussianNB()
    model.fit(Xtrain, ytrain)
    y_model = model.predict(Xtest)
    accuracy=accuracy_score(ytest, y_model)

    print(accuracy)

    mat = confusion_matrix(ytest, y_model)

    sns.heatmap(mat, square=True, annot=True, cbar=False)
    plt.xlabel('predicted value')
    plt.ylabel('true value')
    plt.show()
