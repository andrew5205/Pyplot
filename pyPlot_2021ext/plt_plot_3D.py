# https://matplotlib.org/2.0.2/mpl_toolkits/mplot3d/tutorial.html

# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html


import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d


fig = plt.figure()

# projection='3d
ax = plt.axes(projection='3d')



# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')


plt.show()



############################################################################

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')




