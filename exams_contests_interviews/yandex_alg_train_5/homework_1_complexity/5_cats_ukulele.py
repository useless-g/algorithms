n, k, d = list(map(int, input().split()))
ans = 0

new_n = 10 * n
for digit in range(10):
    new_new_n = new_n + digit
    if new_new_n % k == 0:
        ans = new_new_n
        break

if ans:
    print(f"{ans}{'0' * (d-1)}")
else:
    print(-1)
