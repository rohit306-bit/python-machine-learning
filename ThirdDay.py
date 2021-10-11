import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


ProjectPath = os.getcwd()   #Getting current working directory
print(ProjectPath)

MyFile = ProjectPath + "\\MyData.csv" 
df = pd.read_csv(MyFile)
print(df)

#scatter plot
plt.subplot(2,3,1)
plt.scatter(df['X'],df['Y'])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot Y vs X")
plt.grid()

#line plot
plt.subplot(2,3,2)
plt.plot(df['X'],df['Y'])
plt.scatter(df['X'],df['Y'])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot Y vs X")
plt.grid()

plt.show()

