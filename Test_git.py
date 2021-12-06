import random


def inside(arr, searched):
    i = round(len(arr) / 2)
    steps = 0
    while arr[i] != searched:
        if arr[i] > searched:
            arr = arr[:i]
        else:
            arr = arr[i + 1:]
        steps += 1
        i = round(len(arr) / 2)
        if i == 0 and arr[0] != searched:
            print(f'{searched} not found')
            break
    print(f'{steps} steps were done')


def selection_sort(array):
    result = []
    for i in array:
        min = array[0]
        for j in range(len(array)):
            if array[j] < min:
                min = array[j]
        result.append(min)
        array.remove(min)
    return result


def gcd(a, b):
    while a != b:
        if a > b:
            a, b = b, a - b
        else:
            a, b = a, b - a
    return a


print(gcd(36, 144))
array = []
for i in range(1024):
    array.append(int(random.random() * 10000))
print(array)
array = selection_sort(array)
print(array)
searched = random.choice(array)
print('Search for ', searched)
inside(array, searched)
