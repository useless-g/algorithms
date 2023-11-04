def insertion_sort(arr: list, p, r):
    for j in range(p+1, r+1):
        key = arr[j]
        i = j - 1
        while i >= p and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


def merge(a: list, b: list):
    i = j = 0
    c = [0 for _ in range(len(a) + len(b))]
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # "<=" means stable sort
            c[i+j] = a[i]
            i += 1
        else:
            c[i+j] = b[j]
            j += 1
    while i < len(a):
        c[i+j] = a[i]
        i += 1
    while j < len(b):
        c[i+j] = b[j]
        j += 1
    return c


def merge_sort(a: list):
    if len(a) < 2:
        return  # insertion?
    middle = len(a) // 2
    left = a[:middle]
    right = a[middle:]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    for i in range(len(a)):
        a[i] = c[i]


"""Cormen"""


def kmerge_sort(a, p, r):
    if r < p + 4:
        insertion_sort(a, p, r)
    else:
    # if p < r:
        mid = (p + r) // 2
        kmerge_sort(a, p, mid)
        kmerge_sort(a, mid + 1, r)
        kmerge(a, p, mid, r)


def kmerge(a, p, mid, r):
    left = a[p:mid+1]
    right = a[mid+1:r+1]
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[p+i+j] = left[i]
            i += 1
        else:
            a[p+i+j] = right[j]
            j += 1

    while i < len(left):
        a[p+i+j] = left[i]
        i += 1
    while j < len(right):
        a[p+i+j] = right[j]
        j += 1


if __name__ == "__main__":
    a = [5, 4, 3, 6, 7, 8, 9, 1, 2]
    kmerge_sort(a, 0, len(a)-1)
    print(a)
