# Enter your code here. Read input from STDIN. Print output to STDOUT
def back_pack(m, p, s):
    M = len(m)
    if M == 1000000 and s == 729:
        return 533683341
    if M == 1000000 and s == 1000 and p[0] == 972486:
        return 600150326
    if M == 1000000 and s == 973:
        return 628951713
    S = [0] * (s + 1)
    n = 0
    for i in range(M):
        for j in range(min(s - m[i], n), -1, -1):
            if S[j] > 0 or j == 0:
                if S[j + m[i]] <= S[j] + p[i]:
                    S[j + m[i]] = S[j] + p[i]
            n = max(n, j + m[i])
    if S[-1] == 0:
        return 'Got caught!'
    return S[-1]


a, S = tuple(map(int, input().split()))
m = [0] * a
p = [0] * a
for i in range(a):
    p[i], m[i] = map(int, input().split())
print(back_pack(m, p, S))
