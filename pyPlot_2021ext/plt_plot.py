# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html


import matplotlib.pyplot as plt
import numpy as np


arr_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_y = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

plt.plot(arr_x, arr_y, 'r+')
plt.plot(arr_y, arr_x, 'g*--')


plt.show()



# Other combinations such as [color][marker][line] are also supported, but note that their parsing may be ambiguous.

# Markers
# character	description
# '.'	point marker
# ','	pixel marker
# 'o'	circle marker
# 'v'	triangle_down marker
# '^'	triangle_up marker
# '<'	triangle_left marker
# '>'	triangle_right marker
# '1'	tri_down marker
# '2'	tri_up marker
# '3'	tri_left marker
# '4'	tri_right marker
# '8'	octagon marker
# 's'	square marker
# 'p'	pentagon marker
# 'P'	plus (filled) marker
# '*'	star marker
# 'h'	hexagon1 marker
# 'H'	hexagon2 marker
# '+'	plus marker
# 'x'	x marker
# 'X'	x (filled) marker
# 'D'	diamond marker
# 'd'	thin_diamond marker
# '|'	vline marker
# '_'	hline marker
# Line Styles


# character	description
# '-'	solid line style
# '--'	dashed line style
# '-.'	dash-dot line style
# ':'	dotted line style
# Example format strings:


# 'b'    # blue markers with default shape
# 'or'   # red circles
# '-g'   # green solid line
# '--'   # dashed line with default color
# '^k:'  # black triangle_up markers connected by a dotted line
# Colors



# The supported color abbreviations are the single letter codes
# character	color
# 'b'	blue
# 'g'	green
# 'r'	red
# 'c'	cyan
# 'm'	magenta
# 'y'	yellow
# 'k'	black
# 'w'	white

