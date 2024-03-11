from collections import deque

n = int(input())
all = {}
for i in range(n):
    s = input().split(' ')
    if len(s) == 1:
        all[s[0]] = []
    else:
        all[s[0]] = s[2:]

n = int(input())
for i in range(n):
    a, b = input().split(' ')
    if a not in all or b not in all:
        print("No")
        continue
    if a == b:
        print("Yes")
        continue
    answer = "No"
    parents = deque(all[b])

    while parents:
        parent = parents.popleft()
        if parent == a:
            answer = "Yes"

        parents += all[parent]
    print(answer)
