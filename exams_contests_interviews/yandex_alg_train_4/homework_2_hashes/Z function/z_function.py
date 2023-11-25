# linear
s = input()
n = len(s)
z = [0] * n
for i in range(1, n):
    if s[i] == s[i-1]:
        z[1] += 1
    else:
        break

for i in range(2, n):
    z[i] = z[i + z[i]]
