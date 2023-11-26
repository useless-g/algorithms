from random import randint
from time import time


def karatsuba(x, y):
    """
    Multiply 2 numbers by karatsuba algo.

    Args:
      x: first number to be multiplied.
      y: second number to be multiplied.
    Returns:
      Product of x and y.
    """

    # base case
    if x < 10 or y < 10:
        return x * y
    x = str(x)
    y = str(y)
    n = max(len(x), len(y))
    if n % 2:
        n += 1
    m = n // 2
    x = '0' * (n - len(x)) + x
    y = '0' * (n - len(y)) + y
    # if len(x) < len(y):
    #     x = '0' * (len(y)-len(x)) + x
    # else:
    #     y = '0' * (len(x) - len(y)) + y
    # x_H = (x[m-1:0:-1])[::-1]
    # x_H = x[0] + x_H
    # x_L = x[-1:m - 1:-1][::-1]
    x_H = x[:m]
    x_L = x[m:]

    y_H = y[:m]
    y_L = y[m:]

    x_H = int(x_H)
    x_L = int(x_L)
    y_H = int(y_H)
    y_L = int(y_L)

    a = karatsuba(x_H, y_H)
    d = karatsuba(x_L, y_L)
    e = karatsuba(x_H + x_L, y_H + y_L) - a - d

    return int(str(a) + '0'*m*2) + int(str(e) + '0'*m) + d


k = 0
p = 0
print(karatsuba(627, 313))
print(627 * 313)
for i in range(10):
    aa = randint(10**2000, 10**5000)
    bb = randint(10**2000, 10**5000)
    # if karatsuba(aa, bb) != aa * bb:
    #     print(aa, bb)
    #     break
    s = time()
    aa * bb
    res2 = time() - s
    s = time()
    karatsuba(aa, bb)
    res1 = time() - s
    #
    print(res1, res2)
    if res1 > res2:
        p += 1
    else:
        k += 1
print('karatsuba ', ' python')
print('\t   ', k, ':', p)
