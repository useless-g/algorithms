from math import ceil

t = int(input())
for i in range(t):
    n, a, b = map(int, input().split(" "))
    a, b = min(a, b), max(a, b)

    for j in range(a, b + 1):
        remains = n % j
        doedonchik = j + ceil(remains / (n // j))
        if (remains * doedonchik == 0) or (a <= remains <= b) or (a <= doedonchik <= b):
            print("YES")
            break
    else:
        print("NO")
