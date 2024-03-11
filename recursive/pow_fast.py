from time import time


def simple_loop_pow(a: float, n: int):
    s = 1
    for i in range(1, n + 1):
        s *= a
    return s


def pow_recursive(a: float, n: int) -> float:
    """
    :param a: number
    :param n: degree
    :return: a**n
    """
    if n == 1:
        return a
    elif n % 2:
        return pow(a, n - 1) * a
    return pow(a * a, n // 2)


def fast_pow(a: float, n: int) -> float:
    """
    :param a: number
    :param n: degree
    :return: a**n
    """
    c = 1
    while n > 1:
        if n % 2 == 0:
            a *= a
            n //= 2
        else:
            c *= a
            n -= 1
    return c * a


t = time()
for _ in range(1000):
    1234 ** 12345
print(time() - t)

t = time()
for _ in range(1000):
    simple_loop_pow(1234, 12345)
print(time() - t)

t = time()
for _ in range(1000):
    pow_recursive(1234, 12345)
print(time() - t)

t = time()
for _ in range(1000):
    fast_pow(1234, 12345)
print(time() - t)
