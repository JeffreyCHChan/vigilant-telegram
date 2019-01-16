import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
file = pd.read_excel('C:\\Users\\Jeff\\Downloads\\charging.xlsx', header=1, sheet_name=0, index_col=4)

x = np.arange(0,235.5,0.5) #needs to be fixed to take in the x values of the excel file
y = file.iloc[:,1] #takes first voltage column
z = file.iloc[:,2]#takes second voltage column
a = file.iloc[:,3] #takes third voltage column
plt.plot(x,y) #plots time v voltage
plt.plot(x,z) #plots time v voltage
plt.plot(x,a)#plots time v voltage
plt.show() #displays graph