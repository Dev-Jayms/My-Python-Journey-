"""This build a simple plot"""
import matplotlib.pyplot as plt
import numpy as np

plt.title("James Graph")
plt.xlabel("Calories")
plt.ylabel("Duration(Minutes)")

xpoints = np.array([0,20,35,50,75])
ypoints =np.array([0,30,45,70,120])

plt.plot(xpoints,ypoints)
plt.show()