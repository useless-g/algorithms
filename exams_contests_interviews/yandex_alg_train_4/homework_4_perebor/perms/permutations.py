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


N = int(input())
permutation_generator = permutations(N)
for perm in permutation_generator:
    print("".join(map(str, map(lambda x: x + 1, perm))))