from itertools import permutations


N = int(input())
minE = float("inf")
perms = permutations([i for i in range(N-1)])
graph = [[0] for _ in range(N+1)]
graph[0] += [0 for _ in range(N)]
for i in range(1, N+1):
    l = list(map(int, input().split()))
    minE = min(minE, min(l))
    graph[i] += l

min_path = float("inf")
for perm in perms:
    path = list(perm)
    if len(path) == 0:
        min_path = 0
        break
    path = [1] + list(map(lambda x: x + 2, path)) + [1]
    s = 0
    for i in range(N):
        try:
            if graph[path[i]][path[i+1]]:
                s += graph[path[i]][path[i+1]]
            else:
                break
            if s + (N - i - 1) * minE > min_path:
                break
        except KeyError:
            break
    else:
        min_path = min(min_path, s)

print(min_path if min_path != float("inf") else -1)
