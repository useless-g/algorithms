"""
https://www.codewars.com/kata/55983863da40caa2c900004e
Create a function that takes a positive integer and returns the next bigger number
that can be formed by rearranging its digits.
For example:
  12 ==> 21
 513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1:
  9 ==> -1
111 ==> -1
531 ==> -1
"""

import math
from time import time


def gen_permutations_recursive(N: int, M: int=None, prefix=None):
    M = N if M is None else M
    prefix = prefix or []
    if M == 0:
        # print(''.join(map(str, prefix)))
        return

    for number in range(1, N + 1):
        if number in prefix:
            continue
        prefix.append(number)
        gen_permutations_recursive(N, M-1, prefix)
        prefix.pop()


def next_bigger(n):
    n = list(str(n))
    N = len(n)
    if N < 2:
        return -1

    flag = True
    for i in range(1, N):
        if n[i-1] < n[i]:
            flag = False
            break
    if flag:
        return -1

    for k in range(N-2, -1, -1):
        for j in range(N-1, k-1, -1):
            for i in range(j, k-1, -1):
                if n[j] > n[i - 1]:
                    n.insert(i - 1, str(n[j]))
                    del n[j + 1]
                    n = n[:i] + sorted(n[i:])
                    # return int(''.join(n))
                    perm = ''.join(n)
                    # print(perm)
                    return perm


if __name__ == "__main__":
    t = time()

    s = "0123456789"
    a = math.factorial(10) - 1
    for _ in range(a):
        s = next_bigger(s)

    # gen_permutations_recursive(10)

    print(time() - t)
