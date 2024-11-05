"""
Display Multiple Plots:
This code is used to create a subplot in matplotlib.
With the subplot() function you can draw multiple plots in one figure:
"""

import matplotlib.pyplot as plt
import numpy as np

# Plot 1
x =np.array = ([0,1,2,3])
y = np.array = ([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)

# Plot 2
x =np.array = ([0,1,2,3])
y = np.array = ([3,8,1,10])
plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()
