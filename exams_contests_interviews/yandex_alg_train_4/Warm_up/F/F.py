from math import ceil

k = int(input())
n = int(input())
a = [int(input()) for _ in range(n)]
s = sum(a)
t = 0
cur = len(a) - 1

while s:
    for i in range(cur, -1, -1):
        if a[i] != 0:
            cur = i
            break
    t += (cur + 1) * 2 * ceil(a[cur] / k)  # top floor (+ 1 not full) lift to the bottom
    remains = a[cur] % k
    s -= a[cur]
    a[cur] = 0

    if remains:
        lift = remains
        cur -= 1
        while (lift != k) and (cur > -1):
            while (cur > -1) and (a[cur] == 0):
                cur -= 1
            if a[cur] >= k - lift:
                a[cur] -= k - lift
                s -= k - lift
                lift = k
            elif a[cur] < k - lift:
                lift += a[cur]
                s -= a[cur]
                a[cur] = 0
                cur -= 1
    else:
        cur -= 1

print(t)


