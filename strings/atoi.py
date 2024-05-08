# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        minus = (s[0] == "-")
        if minus or s[0] == "+":
            s = s[1:]
        answer = ""
        i = -1
        char = "0"
        while char == "0":
            i += 1
            try:
                char = s[i]
            except IndexError:
                return 0
        s = s[i:]
        for char in s:
            if not char.isdigit():
                break
            answer += char
        # print(answer)
        if not answer:
            return 0
        s = int(answer)
        if minus:
            s = -s
            s = max(s, -2147483648)
        else:
            s = min(s, 2147483647)
        return s


print(Solution().myAtoi("+1"))
