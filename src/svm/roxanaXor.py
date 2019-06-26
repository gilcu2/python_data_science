import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn import svm
# %matplotlib inline

points = []
y = []
for i in range(100):
    p1, p2 = random.random(), random.random()
    points.append([p1, p2])
    y.append(0 if (p1<=.5 and p2<=.5) or (p1>=0.5 and p2>=0.5) else 1)
X = np.array(points)

clf = svm.SVC(kernel='linear', C=1)

clf.fit(X, y)

w = clf.coef_[0]
interception=clf.intercept_[0]

print("pendiente:", w)
print("intercepto:", interception)

m = -w[0]/w[1]
interc = -interception/w[1]

rect_x = np.linspace(-1,1,100)
rect_y = m*rect_x+interc

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(-1,2)
ax.set_ylim(-1,2)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
X1, Y1 = zip(*[x for i, x in enumerate(X) if y[i]==0])
X2, Y2 = zip(*[x for i, x in enumerate(X) if y[i]==1])
plt.plot(X1, Y1, 'ro')
plt.plot(X2, Y2, 'bo')
plt.plot(rect_x, rect_y, '-g', label=f'y={m}x+{interc}')
plt.show()