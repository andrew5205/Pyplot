
import numpy as np
import matplotlib.pyplot as plt


# matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

f1 = plt.figure(1)
plt.plot(x, y, 'r+')


f2 = plt.figure(2)
plt.plot(x, y, 'bo--')


f31 = plt.figure(31)
plt.plot(x, y, 'go--', linewidth=2, markersize=12)

f32 = plt.figure(32)
plt.plot(x, y , color='green', marker='o', linewidth=2, markersize=12)


# mutiple in one line
f_mult = plt.figure('multiple')
p = np.arange(0, 5, 0.2)
plt.plot(p, p, 'r--', p, p**2, 'bs', p, p**3, 'g^')

plt.show()


# # Format Strings
# fmt = '[marker][line][color]'

# Markers:
# character	description
# '.'	        point marker
# ','	        pixel marker
# 'o'	        circle marker
# 'v'	        triangle_down marker
# '^'	        triangle_up marker
# '<'	        triangle_left marker
# '>'	        triangle_right marker
# '1'	        tri_down marker
# '2'	        tri_up marker
# '3'	        tri_left marker
# '4'	        tri_right marker
# 's'	        square marker
# 'p'     	    pentagon marker
# '*'	        star marker
# 'h'	        hexagon1 marker
# 'H'	        hexagon2 marker
# '+'	        plus marker
# 'x'	        x marker
# 'D'	        diamond marker
# 'd'	        thin_diamond marker
# '|'	        vline marker
# '_'	        hline marker


# Line Styles:
# character	description
# '-'	        solid line style
# '--'	    dashed line style
# '-.'	    dash-dot line style
# ':'	        dotted line style



# Colors - The supported color abbreviations are the single letter codes
# character	color
# 'b'	        blue
# 'g'	        green
# 'r'	        red
# 'c'	        cyan
# 'm'	        magenta
# 'y'	        yellow
# 'k'	        black
# 'w'	        white





