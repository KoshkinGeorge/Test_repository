import random
from math import floor


def merge(arr1, arr2):
    ans = []
    while arr1 != [] and arr2 != []:
        if arr1[0] > arr2[0]:
            ans.append(arr2[0])
            del arr2[0]
        else:
            ans.append(arr1[0])
            del arr1[0]
    return ans + arr1 + arr2


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        return merge(merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2:]))


array = []
for i in range(1024):
    array.append(int(random.random() * 10000))
print(array)
array = merge_sort(array)
print(array)
