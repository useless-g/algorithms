def choice_sort(arr: list, descending: bool = False):
    if descending:
        for i in range(len(arr) - 1):
            max_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] > arr[max_index]:
                    max_index = j
            t = arr[max_index]
            arr[max_index] = arr[i]
            arr[i] = t
    else:  # ascending
        for i in range(len(arr) - 1):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            t = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = t


if __name__ == "__main__":
    a = [6, 5, 4, 0, 3, 4, 3, 2, 1, 0]
    print(a)
    choice_sort(a)
    print(a)
    choice_sort(a, descending=True)
    print(a)
