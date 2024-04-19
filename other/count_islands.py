# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ищем первую землю
        # дальше идем поиском в ширину и ставим в вершину island_number
        # когда закончили ище дальше непомеченную землю и повторяем
        # возвращаем island_number
        island_number = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # unmarked ground
                    neighbors = [(i, j)]
                    while neighbors:
                        # print(neighbors)
                        ii, jj = neighbors.pop()
                        grid[ii][jj] = island_number

                        if (ii != 0) and (grid[ii - 1][jj] == "1"):  # unmarked ground up
                            neighbors.append((ii - 1, jj))
                        if (ii != len(grid) - 1) and (grid[ii + 1][jj] == "1"):  # unmarked ground down
                            neighbors.append((ii + 1, jj))
                        if (jj != len(grid[0]) - 1) and (grid[ii][jj + 1] == "1"):  # unmarked ground right
                            neighbors.append((ii, jj + 1))
                        if (jj != 0) and (grid[ii][jj - 1] == "1"):  # unmarked ground left
                            neighbors.append((ii, jj - 1))
                    island_number += 1
        return island_number



