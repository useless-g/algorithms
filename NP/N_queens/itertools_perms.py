from time import time
from itertools import permutations

for o in range(1, 10):
    t = time()
    N = o

    permutation_generator = permutations(list(range(N)))
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

# 1 1 0.0
# 2 0 0.0
# 3 0 0.0
# 4 2 0.0010001659393310547
# 5 10 0.0
# 6 4 0.004004240036010742
# 7 40 0.031015396118164062
# 8 92 0.30499267578125
# 9 352 2.6540067195892334
