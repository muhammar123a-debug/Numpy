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


#Indexing In array
arr3 = np.array([10,30,40,50,60])
print(arr3[0])
print(arr3[2])
print(arr3[-2])

#Slicing in array
arr4 = np.array([10,20,30,40,50,60,70,80])
#[Start:End:Step]
print(arr4[1:5])
print(arr4[:3])
print(arr4[3:])
print(arr4[::2])
print(arr4[::-2])


#Fency indexing 
arr5 = np.array([10,20,30,40,50,60,70,80])
arr5 = arr5[[1, 3, 5]]
print(arr5)

#Filtering in array
arr6 = np.array([10,25,30,45,50,65,70,85])
filtering = arr6 > 34
print(arr6[filtering])

# reshaping and manipulating arrays
arr7 = np.array([10,25,30,45,50,65,70,85])
reshaped_arr = arr7.reshape(2,4)
print(reshaped_arr)