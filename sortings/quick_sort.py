from time import time


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    less = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]
    return quick_sort(less) + mid + quick_sort(greater)


if __name__ == "__main__":
    array = [i for i in range(1000000 - 1, 0, -1)]
    t = time()
    quick_sort(array)
    print(time() - t)
