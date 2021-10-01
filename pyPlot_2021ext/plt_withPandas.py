import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 



gas = pd.read_csv('./data/gas_prices.csv')
# print(gas)

# plt.figure(figsize=(2,3))

# plt.title('gas price')



plt.plot(gas.Year, gas.USA, 'b.-' ,label='USA')
plt.plot(gas.Year, gas.Canada, 'r*-', label='Canada')
plt.plot(gas['Year'], gas['South Korea'], 'g^-')

plt.title("country gas price", fontdict={'fontweight':'bold', 'fontsize': 20})

# # using loop to display all 
# # make a list first, loop thru that list 
# for country in gas:
#     if country != 'Year':
#         plt.plot(gas.Year, gas[country], marker='.')



plt.xticks(gas.Year[::3])



plt.legend()
plt.show()






