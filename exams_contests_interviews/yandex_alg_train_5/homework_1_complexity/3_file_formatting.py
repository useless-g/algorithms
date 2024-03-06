n = int(input())
ans = 0
for i in range(n):
    s = int(input())
    ans += s // 4
    s %= 4
    if s == 3:
        ans += 2
    else:
        ans += s
print(ans)
