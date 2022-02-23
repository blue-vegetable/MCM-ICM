from pydoc import importfile
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

a = [(1, 3.2), (2, 4.5), (3, 6), (4, 6.5), (7, 9.5),
     (9, 11.1), (11, 13), (14, 14.5), (16, 16), (23, 18.5)]
a = np.array(a)

x = a[:, 0]
y = a[:, 1]


def objective(x, a, b, k):
    return a + b*np.log(x)


popt, _ = curve_fit(objective, x, y)
yvals = objective(x, *popt)

print(popt)
plt.scatter(x, y)
# plt.plot(x, yvals)
plt.show()
