n = int(input())
s = input()
z = [0] * n
z[0] = 1
x_ = 10
p = 10**9 + 7
h = [0] * (n + 1)
h_reversed = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
s = " " + s
for i in range(1, n + 1):
    h[i] = (h[i-1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p
    h_reversed[i] = (h_reversed[i - 1] * x_ + ord(s[-i])) % p


def isequal(from2, slen):
    return (h[slen] + h_reversed[n - from2] * x[slen]) % p == h_reversed[n - from2 + slen]


for i in range(1, n+1):
    low = 0
    high = i + 1
    while high - low > 1:
        mid = (high + low) // 2
        L = mid
        if isequal(i, L):
            low = mid
        else:
            high = mid
    z[i-1] = low


print(" ".join(map(str, z)))
