# -*- coding: utf-8 -*-

# 反转链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        back = None
        cur = fut = head
        while fut:
            fut = fut.next
            cur.next = back
            back = cur
            cur = fut
        return back