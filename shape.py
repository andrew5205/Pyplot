
import numpy as np 
import matplotlib.pyplot as plt


# np.arange(start=, stop=, step=)
p = np.arange(0, 5, 0.2)


# red dashes, blue squares, green triangle
plt.plot(p, p, 'r--', p, p**2, 'bs', p, p**3, 'g^')

plt.show()


















