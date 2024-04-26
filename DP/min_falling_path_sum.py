# https://leetcode.com/problems/minimum-falling-path-sum-ii
class Solution:
    def minFallingPathSum(self, grid):
        n = len(grid)
        dp = grid.pop()
        for i in range(n-1):
            min1 = dp.index(min(dp))
            min2 = dp.index(min(dp[:min1] + dp[min1 + 1:]))
            for j in range(n):
                grid[-1][j] += dp[min1] if j != min1 else dp[min2]
            dp = grid.pop()
        return min(dp)

print(Solution().minFallingPathSum([[0]]))