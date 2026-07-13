import numpy as np
arr1 = np.array([1,2,3,4,5,6],dtype=np.int64)

arr2 = np.array([[1,2,3,4],[5,6,7,8]],dtype=np.int64)

arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]],dtype=np.int64)
print("one D:")
print(arr1)
print("Two D:")
print(arr2)
print(arr2.shape)
print(arr2.data)
print("Three D:")
print(arr3)
print(arr3.shape)
print(arr3.strides)