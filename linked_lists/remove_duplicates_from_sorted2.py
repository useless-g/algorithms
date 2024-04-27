# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None):
            return head
        node = head.next
        last = head
        remove_me = set()

        while node:
            if last.val == node.val:
                last.next = node.next
                node = last.next
                remove_me.add(last.val)
            else:
                last = node
                node = node.next

        while head and (head.val in remove_me):
            head = head.next
        if (head is None) or (head.next is None):
            return head
        node = head.next
        last = head
        while node:
            if node.val in remove_me:
                last.next = node.next
                node = last.next
            else:
                last = node
                node = node.next
        return head
