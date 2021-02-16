# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = cur = head
        back = None
        while pre:
            pre = cur.next
            cur.next = back
            back = cur
            cur = pre
        return back