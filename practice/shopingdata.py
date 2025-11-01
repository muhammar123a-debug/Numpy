import numpy as np

data = np.genfromtxt("shopping_behavior_updated.csv", delimiter=",", skip_header=1)
print(data)
print(data.shape) #Shape is (3900, 18)
print(data.ndim) #dimention is (2)
print(data.dtype) #dtype is float
print(data[:5]) #print 5 rows 
rows, col = data.shape
print("Total Rows : ", rows)
print("Total Column : ", col)
print(data.min())
print(data.max())
print(data.mean())
print(np.isnan(data).count())