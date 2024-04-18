# https://leetcode.com/problems/island-perimeter
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:  # ground
                    if (i == 0) or (not grid[i - 1][j]):  # water up
                        perimeter += 1
                    if (i == len(grid) - 1) or (not grid[i + 1][j]):  # water down
                        perimeter += 1
                    if (j == len(grid[0]) - 1) or (not grid[i][j + 1]):  # water right
                        perimeter += 1
                    if (j == 0) or (not grid[i][j - 1]):  # water left
                        perimeter += 1
        return perimeter
