# https://leetcode.com/problems/add-one-row-to-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque


class Solution:

    # def tree2list(self, root):
    #     result = []
    #     nodes = deque([root])
    #
    #     while nodes:
    #         node = nodes.popleft()
    #         if node is None:
    #             result.append(None)
    #             continue
    #         result.append(node.val)
    #         nodes.append(node.left)
    #         nodes.append(node.right)
    #     return result

    def add_childs(self, root, val):
        if root is None:
            return
        root.left = TreeNode(val=val, left=root.left)
        root.right = TreeNode(val=val, right=root.right)

    def go_deep(self, root, val, real_depth, depth):
        if real_depth == depth - 1:
            self.add_childs(root, val)
            return
        if root is None:
            return
        self.go_deep(root.left, val, real_depth + 1, depth)
        self.go_deep(root.right, val, real_depth + 1, depth)

    def addOneRow(self, root, val: int, depth: int):
        if depth == 1:
            return TreeNode(val=val, left=root)
        self.go_deep(root, val, 1, depth)
        return root


