s = input()
# s_list = list(s)
n = len(s)
z = [0] * n
x_ = 257
p = 10**9 + 7
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
s = " " + s
for i in range(1, n + 1):
    h[i] = (h[i-1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p


def isequal(from1, from2, slen):
    return (
        (h[from1 + slen] + h[from2] * x[slen]) % p ==
        (h[from2 + slen] + h[from1] * x[slen]) % p
    )


for i in range(1, n):
    low = i - 1
    high = n
    while high - low > 1:
        mid = (high + low) // 2
        L = mid - i + 1
        if isequal(0, i, L):
            low = mid
        else:
            high = mid
    z[i] = high - i


print(" ".join(map(str, z)))
