# https://leetcode.com/problems/longest-ideal-subsequence
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # s = tuple(map(lambda x: ord(x) - 97, list(s)))
        dp = [0] * 26
        for i in s:
            m = 0
            i = ord(i) - 97
            for j in range(i-k, i+k+1):
                if 0 <= j <= 25:
                    m = max(m, dp[j])
            dp[i] = m + 1

        return max(dp)

print(Solution().longestIdealString("acfgbd", 2))