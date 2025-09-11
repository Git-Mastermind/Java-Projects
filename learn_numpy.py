import numpy as np


def version():
    return np.__version__

# print(version())


def fruits_array():
    arr = np.array(['strawberry', 'blueberries', 'cherrries', 'dragonfruit'])
    return arr[3]

# print(fruits_array())


def int_and_float_array():
    nums = np.array([1,1.5,1.90,6,7])
    return nums[3]

# print(int_and_float_array()


def zero_dimension_array():
    arr = np.array(42)
    return arr

# print(zero_dimension_array())



def one_dimension_array():
    arr = np.array([1,2,3,4,5])
    return arr

    

# print(one_dimension_array())


def two_dimension_array():
    arr = np.array([1,2,3,4,5], [6,7,8,9,10])
    return arr

    
# print(two_dimension_array())



def three_dimension_array():
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]], [[2,4,6,8,10], [1,3,5,7,9]])
    

# print(three_dimension_array())


def check_dimensions():
    arr0 = np.array(42)
    arr1 = np.array([1,2,3,4,5])
    arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
    arr3 = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[2,4,6,8,10], [1,3,5,7,9]]])

    return np.ndim(arr0), np.ndim(arr1), np.ndim(arr2), np.ndim(arr3)

# print(check_dimensions())

def multi_dimension_array():
    arr = np.array([1,2,3,4,5], ndmin=5)
    return arr, arr.ndim

print(multi_dimension_array())





