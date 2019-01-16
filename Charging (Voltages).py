import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
file = pd.read_excel('C:\\Users\\Jeff\\Downloads\\charging.xlsx', header=1, sheet_name=0, index_col=4)

x = np.arange(0,235.5,0.5)
y = file.iloc[:,1]
z = file.iloc[:,2]
a = file.iloc[:,3]
plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,a)
plt.show()