# https://leetcode.com/problems/isomorphic-strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        for i in range(len(s)):
            d.setdefault(t[i], s[i])
            if d[t[i]] != s[i]:
                return False
        if len(set(d.values())) < len(set(d.keys())):
            return False
        return True


print(Solution().isIsomorphic("foo", "bar"))
