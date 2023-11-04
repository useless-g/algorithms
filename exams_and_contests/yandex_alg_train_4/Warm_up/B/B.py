from math import gcd
a, b, c, d = list(map(int, input().split(" ")))
up = a * d + c * b
down = b * d
g = gcd(up, down)
print(up // g, down // g)
