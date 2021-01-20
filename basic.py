

# pip install matplotlib
import matplotlib.pyplot as plt

f1 = plt.figure(1)
plt.plot([1,2,3,4])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# plt.show()



f2 = plt.figure(2)
plt.plot([1,2,3,4], [1,4,9,16])


f3 = plt.figure('red_dot')
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.sxis(x_min, x_max, y_min,_y_max)
plt.axis([0, 6, 0, 20])



plt.show()