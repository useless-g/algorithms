n = int(input())
students = list(map(int, input().split(" ")))

hate_left = [0 for _ in range(n)]
hate_right = [0 for _ in range(n)]

s = 0
for i in range(1, n):
    s += students[i-1]
    hate_left[i] = students[i] * i - s

s = 0
for i in reversed(range(n - 1)):
    s += students[i + 1]
    hate_right[i] = s - students[i] * (n-1-i)

print(" ".join([str(hate_left[i] + hate_right[i]) for i in range(n)]))
