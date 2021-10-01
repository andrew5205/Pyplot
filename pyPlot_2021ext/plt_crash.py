

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

# #################################################################
# # resixe 
# plt.figure(figsize=(4,2), dpi=300)




#################################################################
# Basic graph 

x = [0, 1, 2, 3]
y = [0, 2, 4, 6]

plt.plot(x, y, label='2x', color='r', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')


# # short hand notation
# fmt = '[color][marker][line]'
# plt.plot(x, y, 'r^--', label='2x')

plt.title('Basic Graph from plot', fontdict={'fontname': 'Comic Scans MS', 'fontsize':15})

plt.xlabel('X-Axis', fontdict={'fontname':'Arial'})
plt.ylabel('Y-Axis')


# X, Y axis trickmarks (scale of the graph)
plt.xticks([0, 1, 2, 3])
plt.yticks([0, 2, 4, 6, 8, 10])

# show label in plt.plot()
plt.legend()

# plt.show()


#################################################################


x2 = np.arange(0,4,0.5)
plt.plot(x2, x2**2, 'g', label='square')

# partical ploting 
plt.plot(x2[:5], x2[:5]**2, 'b--', label='square')


plt.legend()


# # save fig 
# plt.savefig('name.png', dpi=300)



plt.show()







