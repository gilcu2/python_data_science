import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use("ggplot")
from sklearn import svm

# x = [1, 5, 1.5, 8, 1, 9]
# y = [2, 8, 1.8, 8, 0.6, 11]
#
# plt.scatter(x, y)
# plt.show()

# Simetric line

# X = np.array([[0, -4],
#               [0, -3],
#               [0, -2],
#               [0, -1],
#               [0, 1],
#               [0, 2],
#               [0, 3],
#               [0, 4]])
#
# y = [1, 1, 0, 0, 0, 0, 1, 1]

# Xor

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
])

y = [0, 1, 1, 0]

clf = svm.SVC(kernel='linear', C=1.0)

clf.fit(X, y)


w = clf.coef_[0]
interception=clf.intercept_[0]

print("pendiente:", w)
print("intercepto:", interception)


print(clf.predict([[0.58, 0.76]]))

a = -w[0] / w[1]

xx = np.linspace(0, 12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.legend()
plt.show()
