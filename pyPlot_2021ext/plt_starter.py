# https://matplotlib.org/stable/tutorials/introductory/usage.html

import matplotlib.pyplot as plt 
import numpy as np


apl_price = [93, 110, 102, 123]
ms_price = [39, 50, 57, 70]
year = [2000, 2010, 2020, 2030]


# plt.plot(x-axis, y-axis)
plt.plot(year, apl_price)

# merge two sets in one
plt.plot(year, apl_price, year, ms_price)


# change line color 
plt.plot(year, apl_price, 'k', year, ms_price, 'b')

# change line stytle
# plt.plot(year, apl_price, 'r--', year, ms_price, '*g')
plt.plot(year, apl_price, '--r', year, ms_price, 'og')

# plt.scatter(x-axis, y-axis)
plt.scatter(year, ms_price)




# plt.xlabel()
plt.xlabel('Year')
plt.ylabel("stock price")


# custom axis limit
# plt.axis([x_min, x_max, y_min, y_max])
plt.axis([1990, 2050, 10, 150])


plt.show()




####################################################################################################
#  using figure default figsize(6.4, 4.8)
fig1 = plt.figure("can be int or str", figsize=(6.4, 4.8))


#       add_subplot(row, col, chart#)
chart1 = fig1.add_subplot(331)
chart2 = fig1.add_subplot(335)

chart1.plot(year, apl_price)
chart2.scatter(year, ms_price)

plt.show()

####################################################################################################
from matplotlib.ticker import MaxNLocator


fig1 = plt.figure("can be int or str", figsize=(10, 5))


chart1 = fig1.add_subplot(121)
chart2 = fig1.add_subplot(122)


chart1.plot(year, apl_price)
chart1.xaxis.set_major_locator(MaxNLocator(integer=True))

chart2.scatter(year, ms_price)
chart2.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.show()


####################################################################################################
# Tuple packaging
fig2, axes = plt.subplots(3,2,figsize=(10,5))

axes[0,0].scatter(year, ms_price)
axes[2,1].plot(year, apl_price)

plt.show()










