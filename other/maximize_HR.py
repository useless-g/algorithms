"""
https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
"""


def convert(x):
    ans = []
    while x:
        ans.append(x % 7)
        x //= 7

    return [0] * (k - len(ans)) + ans[::-1]


k, m = map(int, input().split())
a = []
answer = 0
for i in range(k):
    a.append(list(map(int, input().strip().split())))
    del a[-1][0]

indexes = (convert(i) for i in range(int("6" * k, base=7) + 1))
i = 0
s_last = s = 0
for perm in indexes:
    try:
        s = max(s, sum([((a[i][perm[i]] % m) ** 2) % m for i in range(k)]) % m)
    except IndexError:
        pass
print(s)
