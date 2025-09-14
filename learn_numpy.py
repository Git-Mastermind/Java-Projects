import numpy as np
import matplotlib.pyplot as mat


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

# print(flatten_array())

def array_iteration():
    arr = np.array([1,2,3,4,5])
    for num in arr:
        print(num)

    
# array_iteration()

def two_dimension_array_iteration():
    arr = np.array([[1,2,3], [4,5,6]])
    for x in arr:
        for y in x:
            print(y)
        


# two_dimension_array_iteration()

def nditer():
    arr = np.array([[1,2,3], [4,5,6]])
    for x in np.nditer(arr):
        print(x)

# nditer()

def op_dtypes():
    arr = [[[1,2,3], [4,5,6]]]
    for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
        print(x)
    
# op_dtypes()

def ndenumerate():
    arr = np.array([[1,2,3], [4,5,6]])
    for idx, x in np.ndenumerate(arr):
        print(idx, x)

# ndenumerate()

def concatenate_arrays():
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])

    concat_arrays = np.concatenate((arr1, arr2))

    return concat_arrays


# print(concatenate_arrays())


arr1 = np.array([[1,2,3], [4,5,6]])
arr2 = np.array([[1,3,5], [2,4,6]])

concat_arrays = np.concatenate((arr1, arr2), axis=1)

# print(concat_arrays)

def stack():
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])

    return np.stack((arr1, arr2))

# print(stack())


def hstack():
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])

    return np.hstack((arr1, arr2))

# print(hstack())


def vstack():
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])

    return np.vstack((arr1, arr2))

# print(vstack())

def dstack():
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])

    return np.dstack((arr1, arr2))


# print(dstack())


def array_split():
    arr = np.array([1,2,3,4,5,6])

    return np.array_split(arr, 2)


# print(array_split())

def two_d_array_split():
    arr = np.array([[1,2], [2,3], [4,5], [6,7], [8,9]])

    return np.array_split(arr, 3)


# print(two_d_array_split())

def hsplit():
    arr = np.array([[0,1], [2,3], [4,5], [6,7], [8,9]])

    return np.hsplit(arr, 2)


# print(hsplit())

def array_search():
    arr = np.array([1,8,2,2,8,5,3,2])
    x = np.where(arr == 2)

    return x


# print(array_search())

def searchsorted():
    arr =  np.array([1,3,4,5])
    x = np.searchsorted(arr, 2, side='left')

    return x


# print(searchsorted())

def multiple_searchsorted_values():
    arr = np.array([1,3,7,9])
    x = np.searchsorted(arr, [2, 6, 8], side='left')

    return x


# print(multiple_searchsorted_values())

def sort_by_value():
    arr = np.array([1,9,2,8,3,7,4,6,5])
    sort_array = np.sort(arr)

    return sort_array


# print(sort_by_value())

def sort_alphabetically():
    fruits_arr = np.array(['banana', 'cherry', 'apple'])
    sort_array = np.sort(fruits_arr)

    return sort_array


# print(sort_alphabetically())

def sort_by_boolean():
    boolean_arr = np.array([True, False, True, False])
    sort_array = np.sort(boolean_arr)

    return sort_array


# print(sort_by_boolean())

def sort_two_d_arrays():
    arr = np.array([[1,2,3], [4,5,6]])
    sort_array = np.sort(arr)

    return sort_array


# print(sort_two_d_arrays())

def filter_array():
    arr = np.array([0,1,2,3,4,5,6,7,8,9])
    filter_booleans = [True, False, True, False, True, False, True, False, True, False]
    newarr = arr[filter_booleans]

    return newarr


# print(filter_array())

def conditional_filter_array():
    arr = np.array([0,1,2,3,4,5,6,7,8,9])
    filter_booleans = []
    
    for element in arr:
        if element % 2 != 0:
            filter_booleans.append(True)
        else:
            filter_booleans.append(False)
    
    newarr = arr[filter_booleans]

    return newarr


# print(conditional_filter_array())


def filter_big_numbers():
    arr = np.array([1,2,3,4,5,6])
    big_nums = arr > 3
    newarr = arr[big_nums]
    return newarr


# print(filter_big_numbers())


def filter_even_numbers():
    arr = np.array([0,1,2,3,4,5,6,7,8,9])

    even_nums = arr % 2 == 0
    even_arr = arr[even_nums]

    return even_arr


# print(filter_even_numbers())

def copy_review():
    arr = np.array([1,2,3,4,5,6])
    arr_copy = arr.copy()
    arr[0] = 5

    return arr_copy


# print(copy_review())

def view_review():
    arr = np.array([1,2,3,4,5,6])
    arr_view = arr.view()
    arr[0] = 5

    return arr_view


# print(view_review())

def shape_review():
    arr = np.array([[1,2,3], [4,5,6]])
    return np.shape(arr)


# print(shape_review())

def graphing():
    x = np.array([0,6])
    y = np.array([1,0])
    mat.plot(y, marker='+')
    mat.show()

graphing()










    












