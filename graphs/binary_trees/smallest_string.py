# https://leetcode.com/problems/smallest-string-starting-from-leaf
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def go_deep(self, root, depth):
        if (depth > self.min_depth) or (root is None):
            return

        self.candidate.append(root.val)
        print(self.candidate, self.candidates, self.min_depth)
        if (root.left is None) and (root.right is None):
            if depth == self.min_depth:
                self.candidates.append(self.candidate[:])
            else:  # depth < self.min_depth
                self.candidates = [self.candidate[:]]
                self.min_depth = depth
        else:
            self.go_deep(root.left, depth + 1)
            self.go_deep(root.right, depth + 1)
        self.candidate.pop()

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        # иметь на каждой итерации минимальную длину
        # глубину захода тоже надо иметь
        # как только глубина захода становится больше минимальной длины мы выходим
        # если длина оказалась меньше чем минимальная то затираем список кандидатов, обновляем минимальную длину
        # когда пройдем все дерево, нужно отсортировать кандидатов и вернуть [0] элемент
        # самое главное:
        # мы должны хранить всю строку до момента пока не упремся в (root.left is None) or (root.right is None)
        # тогда у нас новый кандидат, если длина равна минимальной
        # если не равна то должна быть меньше, то есть обновляем self.min_depth = depth и self.candidates = [root]

        self.min_depth = 8501
        self.candidates = []
        self.candidate = []
        self.go_deep(root, 1)
        return "".join(list(map(lambda x: chr(x + 97), sorted(list(map(lambda x: x[::-1], self.candidates)))[0])))

