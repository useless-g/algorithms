class Solution:
    def findMinHeightTrees(self, n: int, edges):
        self.graph = {}
        self.heights = {}
        for edge in edges:
            self.graph.setdefault(edge[0], {edge[1]}).add(edge[1])
            self.graph.setdefault(edge[1], {edge[0]}).add(edge[0])
        for vertex in self.graph:
            self.heights[vertex] = float("inf")

        self.min_height = float("inf")
        for root in self.graph:
            self.watched = {root}
            self.height = 0
            if not self.go_deep(root) and self.height:
                self.heights[root] = self.height
                self.min_height = min(self.height, self.min_height)

        try:
            min_height = min(self.heights.values())
        except ValueError:
            return [0]
        result = []
        for vertex, height in self.heights.items():
            if height == min_height:
                result.append(vertex)
        return result

    def go_deep(self, root, height=0):
        if height > self.min_height:
            return True
        for vertex in self.graph[root]:
            if vertex in self.watched:
                continue
            self.watched.add(vertex)
            if self.go_deep(vertex, height + 1):
                return True

        self.height = max(self.height, height)
        return True if self.height > self.min_height else False

print(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))


from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        adj_list = defaultdict(set)
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])

        leaves = [i for i in range(n) if len(adj_list[i]) == 1]

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves

sol = Solution()
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))


Этот код обеспечивает те же результаты, что и ваш исходный код, но с использованием более оптимального и эффективного алгоритма.