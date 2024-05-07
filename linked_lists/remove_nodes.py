# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        # return f"val = {self.val}, next = {self.next}"
        return f"{self.val}"
class Solution:
    def removeNodes(self, head):
        node = head.next
        head.next = None
        last = head
        while node:
            next_node = node.next
            node.next = last
            last = node
            node = next_node
        # last is new head
        head = last
        m = last.val
        node = last.next
        while node:
            if node.val < m:
                node = last.next = node.next
            else:
                m = node.val
                last = node
                node = node.next
        node = head.next
        head.next = None
        last = head
        while node:
            next_node = node.next
            node.next = last
            last = node
            node = next_node
        return last

h = ListNode(5)
n = h
for i in [2,13,3,8]:
    h.next = ListNode(i)
    h = h.next

print(Solution().removeNodes(n))