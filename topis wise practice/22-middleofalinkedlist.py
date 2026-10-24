# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pythonforleetcode import ListNode


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        i = j = head
        while i and i.next:
            j=j.next
            i=i.next.next
        return j
            