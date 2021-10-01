import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


fifa = pd.read_csv('./data/fifa_data.csv')
# print(fifa.head(2))

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(fifa.Overall, bins=bins, color='g')

# plt.xticks(bins)

# plt.xlabel('')
# plt.ylabel('')
# plt.title('')






plt.show()


