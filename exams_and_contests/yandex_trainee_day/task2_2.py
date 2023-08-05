def check(s, t):
    dict_s = {}
    dict_t = {}
    for pair in zip(s, t):
        if dict_s.setdefault(pair[0], pair[1]) != pair[1]:
            return 'NO'
        if dict_t.setdefault(pair[1], pair[0]) != pair[0]:
            return 'NO'
    return 'YES'


n = int(input())

for _ in range(n):
    start = input()
    finish = input()
    print(check(start, finish))
