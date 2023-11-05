s = input()
n = len(s)
m = int(input())

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


for i in range(m):
    L, a, b = map(int, input().split(" "))
    print("yes" if isequal(a, b, L) else "no")

