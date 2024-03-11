n = int(input())
arr = tuple(map(int, input().split()))
s = sum(arr)
if s % 2:
    print("+" * (n - 1))
else:
    for i in range(n):
        if abs(arr[i]) % 2:
            x = i + 1
            break
    print("+" * (x - 1), "x", "+" * (n - 1 - x), sep="")

