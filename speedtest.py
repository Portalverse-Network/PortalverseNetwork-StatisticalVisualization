import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# data
df = pd.read_excel('Speedtest.xlsx', sheet_name='sheet1')
country = df['country'].to_numpy()
steam = df['steam'].to_numpy()
ppp = df['ppp'].to_numpy()
uploadbroadband = df['broadband'].to_numpy()

# points
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(steam, ppp, uploadbroadband)

# axis
ax.set_zlabel('broadband(upload)', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('PPP', fontdict={'size': 15, 'color': 'red'})
ax.set_xlabel('steam user count', fontdict={'size': 15, 'color': 'red'})

# label
for i in range(len(steam)):
    ax.text(steam[i], ppp[i], uploadbroadband[i], country[i])

plt.show()