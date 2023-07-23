def power_mod(x: int, y: int, n: int):
    arr = list(map(int, list(str(bin(y))[2:])))[::-1]
    res = 1
    for i in range(len(arr)):
        if arr[i]:
            c = x
            for j in range(i):
                c %= n
                c **= 2
            c %= n
            res = (res * c) % n

    return res


print(power_mod(2, 3 ,5))
print(power_mod(4, 12, 3))
print(power_mod(11, 10, 300))
print(power_mod(11, 100000, 49))
print(power_mod(52345678, 102323230000000, 199898989884675898))
