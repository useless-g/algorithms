from time import time


def count_sort(arr: list, descending: bool = False):
    """
    sorting works if we know domain of array elements, and it is small
    for example: [0:9]
    """
    F = [0 for _ in range(0, max(arr) + 1)]
    for element in arr:
        F[element] += 1
    res = []
    if descending:
        for i in range(len(F)-1, -1, -1):
            for j in range(F[i]):
                res.append(i)
    else:  # ascending
        for i in range(len(F)):
            for j in range(F[i]):
                res.append(i)
    return res


if __name__ == "__main__":
    # a = [6, 5, 4, 0, 3, 4, 3, 2, 1, 0]
    a = [i for i in range(10000000 - 1, 0, -1)]
    # print(a)
    t = time()
    print(count_sort(a))
    print(time() - t)
    # print(count_sort(a, descending=True))
