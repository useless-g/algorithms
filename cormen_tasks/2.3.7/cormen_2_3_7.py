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
    if x > arr[-1] or x < arr[0]:
        return None
    left = binary_search_left(arr, x)
    right = binary_search_right(arr, x)
    if left > right:
        return None
    return left if left == right else (left, right)


def foo(s: list, x) -> bool:
    s = sorted(s)  # O(n*log(n))
    arr = [abs(x - number) if number < x else x - number for number in s]  # O(n)

    for i in range(len(arr)):  # O(n*log(n))
        index = binary_search(s, arr[i])
        if index and index != i:
            return True

    return False


if __name__ == "__main__":
    print(foo([5, 2, 3, 3, 5, 5, 55, 6, -40], -30))
