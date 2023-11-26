N, K = map(int, input().split())
graph = {}
for v in range(1, N+1):
    graph[v] = set()

for _ in range(K):
    a, b, t, w = list(map(int, input().split()))
    graph[a].add((b, t, w))
    graph[b].add((a, t, w))

S = 1
F = N

visited = [True] + [False] * N
weight = [-1] * (N + 1)
weight[S] = 10**7 + 3_000_000
time = [float("inf")] * (N + 1)
time[S] = 0
for i in range(1, N+1):
    index = 0
    max_weight = -1
    for j in range(1, N+1):
        if not visited[j] and weight[j] > max_weight:
            index = j
            max_weight = weight[j]

    for neighbour in graph[index]:
        if (min(max_weight, neighbour[2]) > weight[neighbour[0]]) and (neighbour[1] + time[index] < 1440):
            weight[neighbour[0]] = min(max_weight, neighbour[2])
            time[neighbour[0]] = neighbour[1] + time[index]

    visited[index] = True

print((weight[F] - 3_000_000) // 100)
