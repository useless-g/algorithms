# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        res = 0
        max_res = 0
        for char in s:
            if char not in sub:
                sub.append(char)
                res += 1
            else:
                ind = sub.index(char)
                sub = sub[ind + 1:]
                sub.append(char)
                max_res = res if res >= max_res else max_res
                res = len(sub)
        return res if res >= max_res else max_res


print(Solution().lengthOfLongestSubstring("abcabcbb"))
