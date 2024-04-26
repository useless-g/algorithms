# https://leetcode.com/problems/minimum-falling-path-sum-ii
class Solution:
    def minFallingPathSum(self, grid):
        n = len(grid)
        dp = [[0 for i in range(n)] for j in range(n)]
        dp[0] = grid[0]
        for i in range(1, n):
            for j in range(n):
                m = float("inf")
                for k in range(n):
                    if k == j:
                        continue
                    m = dp[i-1][k] if dp[i-1][k] <= m else m
                dp[i][j] = m + grid[i][j]
        return min(dp[-1])

print(Solution().minFallingPathSum([[0]]))