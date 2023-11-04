n = int(input())
arr = list(map(int, input().split(" ")))
for i in range(1, n - 1):
    if arr[i] < arr[i-1]:
        print(-1)
        break
else:
    print(arr[-1] - arr[0])
