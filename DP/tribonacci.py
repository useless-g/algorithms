# https://leetcode.com/problems/n-th-tribonacci-number
class Solution:
    def tribonacci(self, n: int) -> int:
        a0 = 0
        a1 = 1
        a2 = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        for i in range(2, n):
            t = a0 + a1 + a2
            a0 = a1
            a1 = a2
            a2 = t
        return a2


