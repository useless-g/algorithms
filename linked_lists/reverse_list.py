# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        node = head.next
        head.next = None
        last = head
        while node:
            next_node = node.next
            node.next = last
            last = node
            node = next_node
        # last is new head
        return last
