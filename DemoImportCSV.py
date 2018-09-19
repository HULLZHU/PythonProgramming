import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename = 'StockInfo.csv'
data = pd.read_csv(filename)
print(data)
print(type(data))
array = np.array(data['Price'])
array = array[0:-2]
print(array)
array = [x*2/3for x in array]
print(array)

plt.plot(array)
plt.show()

