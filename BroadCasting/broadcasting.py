import numpy as np

arr1 = np.array([1, 2, 3])
result = arr1 * 2
print(result) 


# 1d to 2d array broadcasting
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10,20,30])
result = arr2 + vector
print(result)