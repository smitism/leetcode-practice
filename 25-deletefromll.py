# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pythonforleetcode import ListNode


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        current = dummy_head

        while current.next!=None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy_head.next