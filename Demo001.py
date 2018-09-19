import numpy as np
arr = np.empty((8,4))
arr = arr.astype(np.int8)
print(arr)
for i in range(8):
    arr[i] = i
print(arr)

arr1 = arr[[4,3,0,6]]
print(arr1)
arr2 = arr[[-3,-5,-7]]
print(arr2)
