# https://leetcode.com/problems/longest-ideal-subsequence
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        s = tuple(map(ord, list(s)))
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            j = i - 1
            while j >= 0:
                if abs(s[i] - s[j]) <= k:
                    dp[i] = max(dp[i], dp[j] + 1)
                j -= 1
            dp[i] = dp[i] if dp[i] else 1

        return max(dp)

print(Solution().longestIdealString("eduktdb", 15))