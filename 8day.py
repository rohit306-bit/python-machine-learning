import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd

MyFile = "D:\PYTHON ML\\DataFile.csv"
df = pd.read_csv(MyFile)
print (df)

x = np.array(df['x'])
y = np.array(df['y'])
Row =2
Col=3
xp = np.linspace(-2,20,100)
plt.subplot(Row,Col,1)
plt.scatter(x,y)
plt.grid()
plt.xlabel("------x--------")
plt.ylabel("------y--------")

plt.subplot(Row,Col,2)
#z = np.polyfit(x, y, Order)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
print("y = ", p)
plt.subplot(Row,Col,2)
plt.plot(x, y, '.')
plt.plot(xp, p(xp), '-')
plt.grid()
plt.xlabel("-------x-------")
plt.ylabel("-------y--------")
plt.title(p)
plt.show()
