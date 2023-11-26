N = int(input())
S, F = map(int, input().split())
R = int(input())

graph = {}
for v in range(1, N+1):
    graph[v] = set()

for _ in range(R):
    a, a0, b, b0 = list(map(int, input().split()))
    graph[a].add((b, a0, b0))

visited = [True] + [False] * N
dist = [float("inf")] * (N + 1)
dist[S] = 0

for i in range(1, N+1):

    index = 0
    min_dist = float("inf")
    for j in range(1, N+1):
        if not visited[j] and dist[j] < min_dist:
            index = j
            min_dist = dist[j]
    if visited[index]:
        break
    for neighbour in graph[index]:
        if (min_dist <= neighbour[1]) and (neighbour[2] < dist[neighbour[0]]):
            dist[neighbour[0]] = neighbour[2]

    visited[index] = True

print(dist[F] if dist[F] != float("inf") else -1)
