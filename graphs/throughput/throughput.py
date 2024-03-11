N, K = map(int, input().split())
graph = {}
for v in range(1, N+1):
    graph[v] = set()

for _ in range(K):
    a, b, t, w = list(map(int, input().split()))
    graph[a].add((b, t, w))
    graph[b].add((a, t, w))

low_weight = 3_000_000 - 1
high_weight = 3_000_000 + 10**9 + 1

S = 1
F = N

while high_weight - low_weight > 1:
    visited = [True] + [False] * N
    time = [float("inf")] * (N + 1)
    time[S] = 0
    weight = (high_weight + low_weight) // 2
    for i in range(1, N+1):
        index = 0
        min_time = float("inf")
        for j in range(1, N+1):
            if not visited[j] and time[j] < min_time:
                index = j
                min_time = time[j]
        if index == 0:
            break

        for neighbour in graph[index]:
            if (min_time + neighbour[1] < time[neighbour[0]]) and (weight <= neighbour[2]):
                time[neighbour[0]] = neighbour[1] + min_time

        visited[index] = True
    if time[F] <= 1440:
        low_weight = weight
    else:
        high_weight = weight

weight = (weight - 3_000_000) // 100
print(weight if weight > 0 else 0)


