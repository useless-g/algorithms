def insertion_sort(arr: list, p, r):
    for j in range(p+1, r+1):
        key = arr[j]
        i = j - 1
        while i >= p and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


def kmerge_sort(a, p, r):
    if r < p + 4:
        insertion_sort(a, p, r)
    else:
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
    n = int(input())
    if n != 0:
        s = input()
        a = list(map(int, s.split(" ")))
        kmerge_sort(a, 0, len(a) - 1)
        print(" ".join(list(map(str, a))))
    else:
        print()