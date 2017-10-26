# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Load the packages needed to complete the script

import numpy as np
import matplotlib.pyplot as plt

# Define the equation and parameters

def ricker (f, length=0.512, dt=0.001):
    t = np.linspace (-length/2, (length-dt)/2, length/dt)
    y = (1.-2.*(np.pi**2)*(f**2)*(t**2))*np.exp(-(np.pi**2)*(f**2)*(t**2))
    return t, y

# Insert the Values

f = 5
t, y = ricker (f)

# Initial plot of the results

plt.plot (t, y)

# Run the program again with added cosmetic improvements

plt.figure (figsize = (7,4))
plt.plot (t, y, lw=2, color='black', alpha=0.5)
plt.fill_between (t, y, 0, y>0.0, interpolate=False, hold=True, color='blue', alpha=0.5)
plt.fill_between (t, y, 0, y<0.0, interpolate=False, hold=True, color='red', alpha=0.5)

# Axis configuration

plt.title ('%d Hz Ricker Wavelet' %f, fontsize=16)
plt.xlabel('Two-way Time (s)', fontsize=14)
plt.ylabel('Amplitude', fontsize=14)
plt.ylim((-1.1,1.1))
plt.xlim((min(t), max(t)))
plt.grid()
plt.show()

# Add formula display

#from sympy import init_session
#from sympy import *
    # y, ricker(f), t = symbols('y f t')
    #str(Integral(sqrt(1/y), y))
#print(latex(Integral(sqrt(1/y), y)))

# unsure how to display the equation in mathematical symbology???
