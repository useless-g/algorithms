from time import time


def next_bigger(n):
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
                    n.insert(i - 1, n[j])
                    del n[j + 1]
                    n = n[:i] + sorted(n[i:])
                    return n


def permutations(N):
    """generator of all permutations of "permutation" numbers"""
    s = list(range(N))
    yield s
    while True:
        s = next_bigger(s)
        if s == -1:
            break
        yield s


for o in range(1, 11):
    t = time()
    N = o

    permutation_generator = permutations(N)
    k = 0
    for perm in permutation_generator:
        flag = True
        for i in range(N):
            if not flag:
                break
            for j in range(N):
                if not flag:
                    break
                if perm[i] != j:
                    continue
                m = i
                n = j
                while m * n > 0:
                    m -= 1
                    n -= 1
                p = -1
                while True:
                    if perm[m] == n:
                        p += 1
                    m += 1
                    n += 1
                    if m > N - 1 or n > N - 1:
                        break
                if p:
                    flag = False
                    break
                m = i
                n = j
                while m != N - 1 and n > 0:
                    m += 1
                    n -= 1
                p = -1
                while True:
                    if perm[m] == n:
                        p += 1
                    m -= 1
                    n += 1
                    if m < 0 or n > N - 1:
                        break
                if p:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            k += 1
    print(o, k, time() - t)
