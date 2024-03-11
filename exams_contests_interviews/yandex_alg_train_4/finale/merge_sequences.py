x = int(input())
i = j = 1
res = 1
while x:
    if i**2 < j**3:
        res = i ** 2
        i += 1
    elif i**2 > j**3:
        res = j ** 3
        j += 1
    else:  # i == j
        res = i ** 2
        i += 1
        j += 1
    x -= 1

print(res)
