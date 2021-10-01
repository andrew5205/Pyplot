# https://matplotlib.org/stable/tutorials/introductory/usage.html

import matplotlib.pyplot as plt
import numpy as np



# pyplot.subplots

fig, ax = plt.subplots()    # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

# plt.show()



##################################################################################
# Figure 

fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes


##################################################################################
# Axes - object (2D - 2 axis, 3D - 3 axis)

# Axes.set_xlim(left=None, right=None, emit=True, auto=False, *, xmin=None, xmax=None)
ax.set_xlim(left=0, right=6)
# Axes.set_ylim(bottom=None, top=None, emit=True, auto=False, *, ymin=None, ymax=None
ax.set_ylim(bottom=0.5, top=5)


# Axes.set_title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs)[source]
# Axes.set_xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)

plt.show()

##################################################################################
# All of plotting functions expect numpy.array or numpy.ma.masked_array as input
# It is best to convert these to numpy.array objects prior to plotting,and to convert a numpy.matrix.

a = pandas.DataFrame(np.random.rand(4, 5), columns = list('abcde'))
a_asarray = a.values

b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)


# ##################################################################################
# Object-oriented
x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.

ax.plot(x, x, label='Linear-OOP')  # Plot some data on the axes.
ax.plot(x, x**2, label='Quadratic-OOP')  # Plot more data on the axes...
ax.plot(x, x**3, label='Cubic-OOP')  # ... and some more.

ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Object Oriented Plot")  # Add a title to the axes.

ax.legend()  # Add a legend.

plt.show()


# ##################################################################################
# pyplot stytle
x = np.linspace(0, 2, 100)

plt.plot(x, x+10, label='linear-plt')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2+10, label='quadratic-plt')  # etc.
plt.plot(x, x**3+10, label='cubic-plt')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("pyplot Plot")

plt.legend()

plt.show()


##################################################################################

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
        The x data

    data2 : array
        The y data

    param_dict : dict
        Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


data1, data2, data3, data4 = np.random.randn(4, 100)
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})

plt.show()



##################################################################################

# plt.gca() - Get the current axes, creating one if necessary.
ax = plt.gca()
ax.plot([3.1, 2.2])

plt.show()




