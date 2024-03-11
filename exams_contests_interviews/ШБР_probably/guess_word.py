s = input()
q = input()
d = {}
answer = ['absent' for i in s]
for i in s:
    if i not in d:
        d[i] = 0
    d[i] += 1
for i in range(len(q)):
    if q[i] == s[i]:
        answer[i] = 'correct'
        d[q[i]] -= 1

for i in range(len(q)):
    if answer[i] != 'correct' and q[i] in d and d[q[i]]:
        d[q[i]] -= 1
        answer[i] = 'present'
    print(answer[i])
