def bubble_sort(arr: list, descending: bool = False):
    if descending:
        for i in range(len(arr)):
            for j in range(len(arr) - 1 - i):
                if a[j] < a[j+1]:
                    tmp = a[j+1]
                    a[j+1] = a[j]
                    a[j] = tmp
    else:  # ascending
        for i in range(len(arr)):
            for j in range(len(arr) - 1 - i):
                if a[j] > a[j+1]:
                    tmp = a[j+1]
                    a[j+1] = a[j]
                    a[j] = tmp

 
if __name__ == "__main__":
    a = [6, 5, 4, 0, 3, 4, 3, 2, 1, 0]
    print(a)
    bubble_sort(a)
    print(a)
    bubble_sort(a, descending=True)
    print(a)
