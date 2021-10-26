#KNN ALGORITHM
'''




'''

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

K=3
x=[7,7,3,1,9,8,7,3]
y=[7,4,4,4,8,3,7,5]
label=[1,1,0,0,1,0,1,0]

features= list(zip(x,y))

print(features)
model = KNeighborsClassifier(n_neighbors=K)
model.fit(features,label)


Query = [3,7]
#perdict output

predicted= model.predict([Query])
print("\nQuery = ", Query)
print("Label = ", predicted)
