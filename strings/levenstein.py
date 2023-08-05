def levenstein(a, b):
    arr = [[i + j if i * j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = min(arr[i - 1][j - 1], arr[i][j - 1], arr[i - 1][j]) + 1
    return arr[-1][-1]

print(levenstein('молоколлллллд', 'колокол'))
