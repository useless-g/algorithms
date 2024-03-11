"""Разбиение Ломуто"""


def partition(A, left, right):
    pivot = A[right]
    j = left
    for i in range(left, right):
        if A[i] > pivot:
            A[i], A[j] = A[j], A[i]
            j += 1
    A[right], A[j] = A[j], A[right]

    return j


def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)


n = 7
a = [1, 3, 9, 8, 2, 7, 5]
quicksort(a, 0, len(a) - 1)
print(a)
