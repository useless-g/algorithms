from copy import deepcopy
from time import time


def get_field():
    a = []
    for i in range(N):
        a.append([])
        for j in range(N):
            a[i].append(1)
    return a


def place_queen(a, i, j):
    res = deepcopy(a)
    length = len(a)
    for k in range(length):
        res[k][j] = 0
    for k in range(length):
        res[i][k] = 0
    k = i
    z = j
    while k >= 0 and z < length:
        res[k][z] = 0
        k += -1
        z += 1
    k = i
    z = j
    while k < length and z < length:
        res[k][z] = 0
        k += 1
        z += 1
    k = i
    z = j
    while k < length and z >= 0:
        res[k][z] = 0
        k += 1
        z += -1
    k = i
    z = j
    while k >= 0 and z >= 0:
        res[k][z] = 0
        k += -1
        z += -1
    return res


def work():
    global counter
    if N == 1:
        counter = 1
        return
    field = get_field()
    for i in range(N):
        temp = place_queen(field, 0, i)
        rec(temp, 1, 0)


def rec(field, str_, count):
    global counter
    if not field[str_].count(1):
        return
    elif str_ == N - 1:
        counter += 1
        return
    for i in range(N):
        if field[str_][i]:
            rec(place_queen(field, str_, i), str_ + 1, count)


for o in range(1, 11):
    t = time()
    counter = 0
    N = o
    work()
    print(o, counter, time() - t)
