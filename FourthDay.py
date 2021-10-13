import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd



'''x = [2, 22, 43, 12, 45, 32, 67, 87, 75]
plt.boxplot(x)
plt.show() '''

plt.subplot(1,3,1)
x = [1, 3, 5, 7]
plt.boxplot(x)

plt.subplot(1,3,2)
x = [1, 3, 5, 7, 29]
plt.boxplot(x)

plt.subplot(1,3,3)
x = [-29, 1, 3, 5, 7]
plt.boxplot(x)

plt.show()

'''
Outlier --> any value that is out of range of the regular data


Movement of Mean ---> Mean is a biased quantity. Mean shifts towards the outlier or mean
is very sensitive towards outlier.

Standard Deviation --->

'''
