import numpy as np

arr1 = np.array([1,2,3])
arr_concat = np.array([1,2,3])
arr2 = np.array([[1,2,3], [4,5,6]])
arr3 = np.array([[[1,2,3], [4,5,6]], [[2,4,6], [1,3,5]]])

concat = np.stack((arr1, arr_concat), axis=2)
print(concat)