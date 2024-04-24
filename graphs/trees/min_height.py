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
