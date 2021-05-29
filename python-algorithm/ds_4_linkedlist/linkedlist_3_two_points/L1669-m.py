# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = list1
        slow = fast = dummy
        for _ in range(b - a + 1):
            fast = fast.next
        for _ in range(a):
            slow = slow.next
            fast = fast.next

        tail_list2 = list2
        while tail_list2.next:
            tail_list2 = tail_list2.next

        slow.next = list2
        tail_list2.next = fast.next
        fast.next = None

        return dummy.next
