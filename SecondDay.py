#important commands for every machine learning datagiven below:

import numpy as np
import pandas as pd

MyFile = "D:\PYTHON ML\TestFile.csv"
df = pd.read_csv(MyFile)
print(df)


'''
A = [2, 34, 32, 45, 21, 56]

Sum = 0
for r in range(0,len(A)):
    Sum = Sum + A[r]
    
Mean = Sum/len(A)
print(A)
print("Mean = ",round(Mean,3))

A = np.array(A)
print("Mean = ",np.mean(A))


print("Mean = ",round(np.mean(A),3))

x = 3.1234
print(x)
print(round(x,3))
'''
