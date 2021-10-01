import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


#################################################################
# Bar chart 
labels = ['A', 'B', 'C']
values = [1, 4, 2 ]

# # traditional way
# plt.bar(labels, values)


# individual - set_hatch()
bars = plt.bar(labels, values)

patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
    
# bars[0].set_hatch('/')
# bars[1].set_hatch('O')
# bars[2].set_hatch('*')


# # figsize=()
# plt.figure(figsize=(6,4))


plt.show()





