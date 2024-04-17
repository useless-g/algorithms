# https://leetcode.com/problems/smallest-string-starting-from-leaf
# top 100% mem!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def go_deep(self, root, depth):
        if root is None:
            return

        self.candidate.append(root.val)
        # print(self.candidate, self.candidates, self.min_depth)
        if (root.left is None) and (root.right is None):
            # self.candidates.append(self.candidate[:])
            self.result = min(self.result, self.candidate[::-1])
        else:
            self.go_deep(root.left, depth + 1)
            self.go_deep(root.right, depth + 1)
        self.candidate.pop()

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.result = [26]
        self.candidate = []
        self.go_deep(root, 1)
        return "".join(list(map(lambda x: chr(x + 97), self.result)))

