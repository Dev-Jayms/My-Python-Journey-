"""
Marker	Description
'o'	Circle
'*'	Star
'.'	Point
','	Pixel
'x'	X
'X'	X (filled)
'+'	Plus
'P'	Plus (filled)
's'	Square
'D'	Diamond
'd'	Diamond (thin)
'p'	Pentagon
'H'	Hexagon
'h'	Hexagon
'v'	Triangle Down
'^'	Triangle Up
'<'	Triangle Left
'>'	Triangle Right
'1'	Tri Down
'2'	Tri Up
'3'	Tri Left
'4'	Tri Right
'|'	Vline
'_'	Hline


Line Reference
Line Syntax	Description
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line


Color Reference
Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White



"""

import matplotlib.pyplot as plt
import numpy as np

# You can use the keyword argument marker to emphasize each point with a specified marker:

# Arrays
xpoints = np.array([3, 28, 10, 10,4, 15,12,16])
ypoints = np.array([2, 16, 13, 12,6, 9,14,18])

# Title
plt.title("James Matplotlib Graph")

# Labels
plt.xlabel("Calories")
plt.ylabel("Duration(Minutes)")

# Markers
# X,Y Plots
plt.plot(xpoints, marker = 'd')
plt.plot(ypoints, 'd:r')

# Display
plt.show()