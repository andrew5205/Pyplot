
import numpy as np
import matplotlib.pyplot as plt


# matplotlib.pyplot.subplot(*args, **kwargs)

# subplot(nrows, ncols, index, **kwargs)
# subplot(pos, **kwargs)
# subplot(**kwargs)
# subplot(ax)


# plt.figure(figsize=(9, 3))

names = ['A', 'B', 'C']
values = [1, 10, 100]

f1 = plt.figure('1X3', figsize=(9, 3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('subplot Plotting 1X3')
# plt.show()




f2 = plt.figure('3X3', figsize=(12, 3))
plt.subplot(331)
plt.bar(names, values)
plt.subplot(335)
plt.scatter(names, values)
plt.subplot(339)
plt.plot(names, values)
plt.suptitle('subplot Plotting 3X3')
plt.show()




