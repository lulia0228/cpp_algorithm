# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = headA, headB
        while l1 != l2:
            if l1 == None:
                l1 = headB
            else:
                l1 = l1.next
            if l2 == None:
                l2 = headA
            else:
                l2 = l2.next
        return l1