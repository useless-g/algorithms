from time import time


def simple_loop_pow(a: float, n: int):
    s = 1
    for i in range(1, n + 1):
        s *= a
    return s


def pow_recursive(a: float, n: int):
    if n == 1:
        return a
    elif n % 2:
        return pow(a, n - 1) * a
    return pow(a * a, n // 2)


t = time()
for _ in range(100):
    1234 ** 1234
print(time() - t)
t = time()
for _ in range(100):
    simple_loop_pow(1234, 1234)
print(time() - t)
t = time()
for _ in range(100):
    pow_recursive(1234, 1234)
print(time() - t)
