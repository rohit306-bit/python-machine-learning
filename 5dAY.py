import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

ProjectPath = os.getcwd()   #Getting current working directory
print(ProjectPath)

MyFile = ProjectPath + "\\DataFolder\\TestData_1.csv" 
df = pd.read_csv(MyFile)
print(df)

print("Mean:")
print(df.mean(axis=0))

print("\nStandard Deviation:")
print(df.std(axis=0))


print("\nVariance")
print(df.var(axis=0))

print("\nMedian:")
print(df.median(axis=0))


