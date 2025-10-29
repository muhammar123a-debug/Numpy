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

#Inserting elements
arr8 = np.array([10,20,30,40,50])
new_arr = np.insert(arr8, 2, 46)
print(new_arr)

# Inserting 2d array
arr9 = np.array([[1,2,3],[4,5,6]])
new_arr2d = np.insert(arr9, 1, [1,6,9], axis=0)
print(new_arr2d)

#appending elements
arr10 = np.array([10,20,30])
arr_appended = np.append(arr10, [40,50,60])
print(arr_appended)

#concatenation of arrays
arr11 = np.array([1,2,4])
arr12 = np.array([5,8,6])

arr_concatenantion = np.concatenate((arr11, arr12))
print(arr_concatenantion)

#removing elements 
arr13 = np.array([10,20,30,40,50])
arr_removed = np.delete(arr13, 2)
print(arr_removed)

#removing from 2d array
arr14 = np.array([[1,2,3],[4,5,6]])
arr_removed_2d = np.delete(arr14, 0, axis=0)
print(arr_removed_2d)

# Stacks 
arr15 = np.array([1,2,3])
arr16 = np.array([4,5,6])
arr_stacks = np.vstack((arr15,arr16))
print(arr_stacks)
arr_stacks = np.hstack((arr15,arr16))
print(arr_stacks)

#Splitting arrays
arr17 = np.array([10,20,30,40,50,60])
print(np.split(arr17, 3))
