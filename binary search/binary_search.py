def binary_search_left(arr, x):
    low = -1
    high = len(arr)
    while high - low > 1:
        mid = (low + high) // 2
        if x > arr[mid]:
            low = mid
        else:
            high = mid
    return high


def binary_search_right(arr, x):
    low = -1
    high = len(arr)
    while high - low > 1:
        mid = (low + high) // 2
        if x >= arr[mid]:
            low = mid
        else:
            high = mid
    return low

def binary_search(arr, x):
    for i in range(1, len(arr)):
        assert (arr[i-1] <= arr[i]), "Array is not sorted!"
    assert (x >= arr[0]), "Element is not in array!"
    assert (x <= arr[-1]), "Element is not in array!"
    left = binary_search_left(arr, x)
    right = binary_search_right(arr, x)
    return left if left == right else (left, right)

if __name__ == "__main__":
    array = [0, 0, 0, 2, 3, 4, 4, 4, 4, 5, 6, 77, 88, 100]
    print(binary_search(array, 4))
    print(binary_search(array, 77))
