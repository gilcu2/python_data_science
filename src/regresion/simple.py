import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    # Data
    rng = np.random.RandomState(42)
    x = 10 * rng.rand(50)
    y = 2 * x - 1 + rng.randn(50)

    #Show
    # plt.scatter(x, y)
    # plt.show()

    #Model
    model = LinearRegression(fit_intercept=True)
    X=x[:,np.newaxis]  # Transform to matrix

    #Fit
    model.fit(X,y)
    print(f"Intercept: {model.intercept_} Coef: {model.coef_}")

    #Predict
    xfit = np.linspace(-1, 11)
    Xfit = xfit[:, np.newaxis]
    yfit = model.predict(Xfit)

    # Results
    plt.scatter(x, y)
    plt.plot(xfit, yfit)
    plt.show()