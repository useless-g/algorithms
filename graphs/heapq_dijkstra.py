import heapq

N, K = map(int, input().split())
graph = {}
for v in range(1, N+1):
    graph[v] = set()

for _ in range(K):
    a, b, l = list(map(int, input().split()))
    graph[a].add((b, l))
    graph[b].add((a, l))


S, F = map(int, input().split())

visited = [True] + [False] * N
dist = [float("inf")] * (N + 1)
dist[S] = 0
dist_heap = [(0, S)]
heapq.heapify(dist_heap)

for i in range(1, N+1):
    for j in range(len(dist_heap)):
        min_dist, index = heapq.heappop(dist_heap)
        if visited[index]:
            continue
        break
    else:
        break

    for neighbour in graph[index]:
        if min_dist + neighbour[1] < dist[neighbour[0]]:
            dist[neighbour[0]] = min_dist + neighbour[1]
            heapq.heappush(dist_heap, (dist[neighbour[0]], neighbour[0]))

    visited[index] = True

print(dist[F] if dist[F] != float("inf") else -1)
