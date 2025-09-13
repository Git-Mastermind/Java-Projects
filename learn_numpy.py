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

# print(multi_dimension_array())

def adding_elements_in_array():
    arr = np.array([1,2,3,4,5])
    return arr[0] + arr[1]

# print(adding_elements_in_array())

def access_two_d_elements():
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
    return arr[0,1]

# print(access_two_d_elements())

def access_3_d_elements():
    arr = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[2,4,6,8,10], [1,3,5,7,9]]])
    return arr[1,0,3]

# print(access_3_d_elements())

def slicing_array():
    arr = np.array([1,2,3,4,5,6,7,8,9,10])
    return arr[1:8:2]

# print(slicing_array())

def dtype_of_array():
    arr = np.array([1,2,3,4,5])
    return arr.dtype

# print(dtype_of_array())

def dtype_of_str_array():
    arr = np.array(['strawberries', 'blueberries', 'dragonfruit'])
    return arr.dtype

# print(dtype_of_str_array())

def change_dtype_of_array():

    arr = np.array([1,2,3,4,5])


    newarr = arr.astype(dtype='f')

    return arr, newarr

# print(change_dtype_of_array())



def copy():
    arr = np.array([1,2,3,4,5,42])
    copy_of_array = arr.copy()
    arr[5] = 6
    return arr, copy_of_array, copy_of_array.base

# print(copy())


def view():
    arr = np.array([1,2,3,4,5,42])
    view_of_array = arr.view()
    arr[5] = 6
    return arr, view_of_array, view_of_array.base 

# print(view())



def reshape():
    arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    newarr = arr.reshape(4,3)
    return newarr

# print(reshape())


def flatten_array():
    arr = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[2,4,6,8,10], [1,3,5,7,9]]])
    flattened_arr = arr.reshape(-1)
    return flattened_arr

print(flatten_array())






