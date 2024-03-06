g11, g21 = list(map(int, input().split(":")))
g12, g22 = list(map(int, input().split(":")))

gost = int(input())

g1_all = g11 + g12
g2_all = g21 + g22

if g2_all == g1_all:
    if gost == 1:
        if g12 > g21:
            ans = 0
        else:
            ans = 1
    elif gost == 2:
        if g11 > g22:
            ans = 0
        else:
            ans = 1
elif g1_all > g2_all:
    ans = 0
else:  # g1_all < g2_all
    ans = g2_all - g1_all
    g12 += g2_all - g1_all
    if gost == 1:
        if g12 > g21:
            ans += 0
        else:
            ans += 1
    elif gost == 2:
        if g11 > g22:
            ans += 0
        else:
            ans += 1

print(ans)
