import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


fifa = pd.read_csv('./data/fifa_data.csv')




left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]


label = ['Left', 'Right']
color = ['#aaddcc', '#abcdef']

plt.pie([left, right], labels=label, colors=color, autopct='%.2f%%')

plt.show()

