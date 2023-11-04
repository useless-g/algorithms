from collections import deque

n = int(input())
students = deque(map(int, input().split(" ")))

hate = []

for i in range(n):
    new_deque = deque()
    student = students.popleft()
    for j in range(n-i-1):
        new_deque.append(abs(student - students[j]))
    s = sum(new_deque)
    for j in range(i):
        s += hate[j].popleft()
    print(s, end=" ")
    hate.append(new_deque)



n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

for i in range(n):
    dissatisfaction = (i * a[i] - prefix_sum[i]) + ((prefix_sum[n] - prefix_sum[i + 1]) - (n - i - 1) * a[i])
    print(dissatisfaction, end=' ')