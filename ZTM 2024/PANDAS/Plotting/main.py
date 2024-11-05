"""
Pandas uses the plot() method to create diagrams.

We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
# df.plot()
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories') #This create a scatter plot graph
df.plot(kind = 'hist') #This create a histogram plot graph

plt.show()
