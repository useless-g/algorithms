from random import randint


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[randint(0, len(arr) - 1)]
    less = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]
    return quick_sort(less) + mid + quick_sort(greater)


n = int(input())
if n == 0:
    print()
else:
    s = input()
    array = list(map(int, s.split(" ")))
    print(" ".join(list(map(str, quick_sort(array)))))
