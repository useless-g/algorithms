N, S, F = map(int, input().split())
visited = [True] + [False] * N
dist = [float("inf")] * (N + 1)
graph = [[0] for _ in range(N+1)]
graph[0] += [0 for _ in range(N)]
for i in range(1, N+1):
    s = list(map(int, input().split()))
    graph[i] += s

dist[S] = 0
for i in range(1, N+1):
    index = 0
    min_dist = float("inf")
    for j in range(1, N+1):
        if not visited[j] and dist[j] < min_dist:
            index = j
            min_dist = dist[j]



    for j in range(1, N + 1):
        if graph[index][j] >= 0 and (graph[index][j] + min_dist < dist[j]):
            dist[j] = graph[index][j] + min_dist

    visited[index] = True

print(dist[F] if dist[F] != float("inf") else -1)
