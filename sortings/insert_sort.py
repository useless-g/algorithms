def insert_sort(arr: list, descending: bool = False):
    if descending:
        for j in range(1, len(arr)):
            key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] < key:
                arr[i + 1] = arr[i]
                i -= 1
            arr[i + 1] = key
    else:  # ascending
        for j in range(1, len(arr)):
            key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i -= 1
            arr[i + 1] = key


if __name__ == "__main__":
    a = [6, 5, 4, 0, 3, 4, 3, 2, 1, 0]
    print(a)
    insert_sort(a)
    print(a)
    insert_sort(a, descending=True)
    print(a)
