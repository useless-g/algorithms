# https://leetcode.com/problems/find-if-path-exists-in-graph
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        result = False
        for edge in edges:
            graph.setdefault(edge[0], {edge[1]}).add(edge[1])
            graph.setdefault(edge[1], {edge[0]}).add(edge[0])
        queue = [source]
        watched = set()
        while queue:
            vertex = queue.pop()
            watched.add(vertex)
            if vertex == destination:
                result = True
                break
            for v in graph[vertex]:
                if v not in watched:
                    queue.append(v)
        return result
