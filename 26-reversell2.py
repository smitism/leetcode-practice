# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pythonforleetcode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy_head = ListNode(-1,head)
        left_prev = dummy_head
        curr = head
        for i in range(left - 1):
            left_prev = curr
            curr = curr.next
        prev = None
        for i in range(right - left +1):
            new = curr.next
            curr.next = prev
            prev = curr 
            curr = new
        left_prev.next.next = curr
        left_prev.next = prev
        return dummy_head.next

