from time import time


def next_bigger_recursive(n: int, length: int, prefix=None):
    """generate all numbers in n notation"""
    if length == 0:
        print(''.join(list(map(str, prefix))))
        return
    prefix = prefix or []
    for digit in range(n):
        prefix.append(digit)
        next_bigger_recursive(n, length - 1, prefix)
        prefix.pop()


if __name__ == "__main__":
    t = time()
    a = 7
    next_bigger_recursive(a, a)
    print(time() - t)



