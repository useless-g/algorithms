n = int(input())
arr = tuple(map(int, input().split()))
for i in range(2**(len(arr)-1)):
    operators = bytes(i, )
    for i in range(2 ** (len(arr) - 1)):
