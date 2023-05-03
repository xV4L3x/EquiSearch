#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 20:00:14 2023

@author: valeriopiodenicola
"""

import numpy as np
import matplotlib.pyplot as plt

'''PARAMETERS'''

#Starting point
P = (4,5)
#Direction of research (Angular coefficient)
m = 1
#lenght of the step
l = 2
#Sign of the research: 1 upwards, -1 downwards
d = -1
#Number of points to be found
n = 15


'''ALG'''

#Slope of research
r = lambda x: m*(x-P[0]) + P[1]

#Array of points
points = [P]

for i in range(n-1):
    #Get x of the new point with valex formula
    qx = np.sign(d) * (l / np.sqrt(1+m**2)) + P[0]
    #Get y of new point using the slope
    qy = r(qx)
    #Save the point in the array
    points.append((qx, qy))
    #Set the reference to the new point
    P = (qx, qy)
    

'''PLOT'''
    
#AXIS
plt.axhline(0, color="black")
plt.axvline(0, color="black")
#Slope
plt.plot(np.linspace(-20, 20, 200), r(np.linspace(-20, 20, 200)))
#Points
for p in points:
    plt.scatter(p[0],p[1])
plt.show()
