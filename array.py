#Shape in Arrays 
import numpy as np

arr_2d = np.array([[22,43,55],[65,76,67]])
print(arr_2d.shape)

#Size total number of elements in array
print(arr_2d.size)

#Number of dimensions
print(arr_2d.ndim)

#data type of elements in array
print(arr_2d.dtype)

#astype 
arr = np.array([1.2, 3.2, 2.4])
print(arr.dtype)
int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)

#operators in numpy
arr1 = np.array([1,2,3])
print(arr1 + 2)  # Addition
print(arr1 * 2)  # Multiplication
print(arr1 ** 2)  # Exponentiation
print(arr1 - 2)  # Subtraction
print(arr1 / 2)  # Division
print(arr1 % 2)  # Modulus

# aggregation functions
# Sum Function
print(np.sum(arr1))  # Sum of all elements
print(np.min(arr1))  # Sum of all elements
print(np.max(arr1))  # Sum of all elements
print(np.mean(arr1))  # Sum of all elements
print(np.std(arr1))  # Sum of all elements
