n = int(input())

last = list(map(int, input().strip().split(":")))
k = 1
for i in range(n - 1):
    s = list(map(int, input().strip().split(":")))
    if s[0] < last[0]:
        k += 1
    elif s[0] == last[0] and s[1] < last[1]:
        k += 1
    elif s[0] == last[0] and s[1] == last[1] and s[2] < last[2]:
        k += 1
    elif s == last:
        k += 1
    last = s
print(k)
"""
5
00:00:00
00:01:11
02:15:59
23:59:58
23:59:59
"""