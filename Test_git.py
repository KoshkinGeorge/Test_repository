import random


def quick_sort(arr):
    equal = []
    less = []
    higher = []
    if arr == []:
        return []
    chosen = random.choice(arr)
    for i in arr:
        if i < chosen:
            less.append(i)
        elif i == chosen:
            equal.append(i)
        else:
            higher.append(i)
    return quick_sort(less) + equal + quick_sort(higher)


array = []
for i in range(1024):
    array.append(int(random.random() * 10000))
print(array)
array = quick_sort(array)
print(array)
