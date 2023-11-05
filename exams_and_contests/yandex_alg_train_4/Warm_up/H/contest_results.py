from math import ceil

a = int(input())
b = int(input())
n = int(input())

maxa = a

minb = ceil(b / n)

print("Yes" if maxa > minb else "No")
