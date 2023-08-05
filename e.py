def swaps(v):
    sorted_v = sorted(v)
    n = len(v)

    m = {}
    for i in range(n):
        m[v[i]] = i

    swaps_count = 0
    for i in range(n):
        expected = sorted_v[i]
        if expected != v[i]:
            swaps_count += 1
            expected_pos = m[expected]
            m[v[i]] = expected_pos
            v[i], v[expected_pos] = v[expected_pos], v[i]

    return swaps_count


n = int(input())
v = list(map(int, input().split()))
reversed_v = list(reversed(v))
print(min(swaps(v), swaps(reversed_v)))